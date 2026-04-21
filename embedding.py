from langchain_community.embeddings import FakeEmbeddings

def get_embedding_model():
    # Simple local embeddings (no downloads, no SSL issues)
    return FakeEmbeddings(size=384)