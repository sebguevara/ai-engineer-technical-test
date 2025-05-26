from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from app.config import OPENAI_API_KEY
from app.utils.get_links import get_internal_links

def build_vectorstore(url="https://promtior.ai"):
    urls = get_internal_links(url)
    loader = WebBaseLoader(web_paths=urls)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return FAISS.from_documents(docs, embeddings)

vectorstore = build_vectorstore()

def get_vectorstore():
    return vectorstore

