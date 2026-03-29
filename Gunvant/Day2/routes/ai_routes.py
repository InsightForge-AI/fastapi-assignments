from fastapi import APIRouter
from Day2.models.query_model import Query
from Day2.services.ai_service import get_ai_response

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello Sahil 🚀"}

@router.post("/ask")
def ask(data: Query):
    return {"your_question": data.question}

@router.get("/health")
def health():
    return {"status": "running"}

@router.post("/ai")
def ai(data: Query):
    answer = get_ai_response(data.question)
    return {"answer": answer}