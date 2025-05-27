from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from app.services.vectorstore import get_vectorstore
from langchain.prompts import PromptTemplate
from app.chains.prompts.rag_prompt import RAG_PROMPT
from app.config import OPENAI_API_KEY

prompt = PromptTemplate(template=RAG_PROMPT)


def get_retrieval_qa_chain():
    retriever = get_vectorstore().as_retriever()
    return RetrievalQA.from_llm(
        llm=OpenAI(openai_api_key=OPENAI_API_KEY),
        retriever=retriever,
        prompt=prompt,
    )
