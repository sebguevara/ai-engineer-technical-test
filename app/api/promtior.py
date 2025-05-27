from fastapi import APIRouter
from langserve import add_routes
from app.chains.retrieval_data import get_retrieval_qa_chain

router = APIRouter()

chain = get_retrieval_qa_chain()
add_routes(router, chain, path="/promtior", input_type=str, output_type=str)
