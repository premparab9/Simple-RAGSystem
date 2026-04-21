# 🚀 RAG System using FastAPI

A complete **Retrieval-Augmented Generation (RAG)** system that allows users to upload PDF documents and ask questions based on their content using a custom LLM API.

---

## 📌 Features

- 📄 Upload PDF documents via API
- 🔍 Extract and split document content
- 🧠 Store embeddings using FAISS
- 🤖 Query documents using LLM (company-hosted OpenAI-compatible API)
- ⚡ FastAPI backend with interactive Swagger UI
- 🔐 Secure API key handling using `.env`

---

## 🏗️ Project Structure
RAG-SYSTEM/
│── app/
│ ├── main.py
│ ├── ingestion.py
│ ├── embedding.py
│ ├── database.py
│ ├── retrieval.py
│ ├── generator.py
│
│── data/ # Uploaded PDFs (ignored in git)
│── .env # API keys (ignored in git)
│── requirements.txt
│── README.md

## Setup

### 1. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=your_base_url
OPENAI_MODEL=your_model_name

uvicorn app.main:app --reload
