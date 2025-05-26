from langchain_community.document_loaders import WebBaseLoader, RecursiveUrlLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import OPENAI_API_KEY

class VectorStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            loader = WebBaseLoader("https://promtior.ai")
            docs = loader.load()
            embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
            cls._instance = FAISS.from_documents(docs, embeddings)
        return cls._instance

def get_vectorstore():
    return VectorStore()