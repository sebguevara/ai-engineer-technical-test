from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from app.config import OPENAI_API_KEY
from app.utils.get_links import crawl_site

PDF_PATH = "data/ai_engineer.pdf"


def build_vectorstore(url="https://promtior.ai"):
    try:
        urls = crawl_site(url)
        web_loader = WebBaseLoader(web_paths=urls)
        pdf_loader = PyPDFLoader(PDF_PATH)
        docs = web_loader.load() + pdf_loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_documents(docs)
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        return FAISS.from_documents(docs, embeddings)
    except Exception as e:
        print(f"Error to build vectorstore: {e}")
        return None


class VectorStore:
    _instance = None

    @classmethod
    def get_instance(cls, url="https://promtior.ai"):
        if cls._instance is None:
            cls._instance = build_vectorstore(url)
        return cls._instance.as_retriever()
    
