from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import hashlib  # ✅ ใช้เพื่อทำให้สุ่มแบบคงที่

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
    # สร้าง seed จาก hash ของคำตอบ
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
        feedback = "คำตอบชัดเจน ครอบคลุมดีมาก"
    elif word_count >= 40:
        score = deterministic_score(answer_text, 70, 85)
        feedback = "อธิบายได้ดีระดับหนึ่ง เหลือรายละเอียดบางจุด"
    elif word_count >= 20:
        score = deterministic_score(answer_text, 50, 70)
        feedback = "คำตอบเริ่มมีแนวคิดที่ดี แต่ยังขาดความชัดเจน"
    else:
        score = deterministic_score(answer_text, 0, 40)
        feedback = "ควรอธิบายให้ชัดเจนมากขึ้น เช่น การทำงานหรือประโยชน์ของ ML"

    return {
        "score": score,
        "feedback": feedback
    }

@app.get("/")
def read_root():
    return {"message": "👋 Welcome to the AI Autograde Backend!"}
