from fastapi import APIRouter
from langserve import add_routes
from app.chains.retrieval_data import get_retrieval_qa_chain
from app.schemas.rag import RAGRequest, RAGResponse
router = APIRouter()

chain = get_retrieval_qa_chain()
add_routes(router, chain, path="/promtior", input_type=RAGRequest, output_type=RAGResponse)
