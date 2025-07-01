from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from grading.grader import grade_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnswerRequest(BaseModel):
    chapter: int
    question: int
    answer: str

@app.post("/api/grade")
def grade(req: AnswerRequest):
    score, similarity, feedback = grade_answer(req.chapter, req.question, req.answer)
    return {
        "score": score,
        "similarity": round(similarity, 2),
        "feedback": feedback
    }
