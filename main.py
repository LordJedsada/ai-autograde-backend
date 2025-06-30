from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import hashlib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnswerRequest(BaseModel):
    answer: str

def deterministic_score(seed_text, min_score, max_score):
    hash_digest = hashlib.sha256(seed_text.encode()).hexdigest()
    seed = int(hash_digest, 16)
    rng = random.Random(seed)
    return rng.randint(min_score, max_score)

@app.post("/api/grade")
def grade_answer(request: AnswerRequest):
    answer_text = request.answer.strip()
    word_count = len(answer_text.split())

    if word_count >= 60:
        score = deterministic_score(answer_text, 85, 100)
        feedback = "Clear and comprehensive explanation."
    elif word_count >= 40:
        score = deterministic_score(answer_text, 70, 85)
        feedback = "Good explanation with some missing details."
    elif word_count >= 20:
        score = deterministic_score(answer_text, 50, 70)
        feedback = "Basic idea is present but lacks clarity."
    else:
        score = deterministic_score(answer_text, 0, 40)
        feedback = "Needs clearer explanation, such as ML usage or concepts."

    return {
        "score": score,
        "feedback": feedback
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Autograde Backend"}
