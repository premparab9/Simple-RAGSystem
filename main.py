from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import os

from app.ingestion import load_and_split
from app.embedding import get_embedding_model
from app.database import create_vector_store
from app.retrieval import get_retriever
from app.generator import get_qa_chain

load_dotenv()

app = FastAPI()

vector_db = None
qa_chain = None

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global vector_db, qa_chain

    os.makedirs("data", exist_ok=True)
    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    chunks = load_and_split(path)
    embedding_model = get_embedding_model()
    vector_db = create_vector_store(chunks, embedding_model)

    retriever = get_retriever(vector_db)
    qa_chain = get_qa_chain(retriever)

    return {"message": "PDF uploaded"}

@app.get("/ask")
def ask(query: str):
    if qa_chain is None:
        return {"error": "Upload a PDF first"}

    return {"answer": qa_chain(query)}