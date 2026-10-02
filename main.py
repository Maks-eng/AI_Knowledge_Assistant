from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="AI Knowledge Assistant",
    description="AI-powered knowledge assistant with RAG",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/info")
def app_info():
    return {
        "name": "AI Knowledge Assistant",
        "version": "0.1.0",
        "status": "development",
    }


class Question(BaseModel):
    question: str


@app.post("/api/ask")
def ask_question(data: Question):
    return {
        "question": data.question,
        "answer": "AI response will be implemented soon."
    }