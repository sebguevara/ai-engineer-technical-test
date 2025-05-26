from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from app.config import OPENAI_API_KEY
from app.services.vectorstore import get_vectorstore

def get_retrieval_qa_chain():
    retriever = get_vectorstore().as_retriever()
    return RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=OPENAI_API_KEY),
        chain_type="stuff",
        retriever=retriever
    )