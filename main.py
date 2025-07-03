from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

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

# ✅ สร้าง endpoint สำหรับให้คะแนนคำตอบ
@app.post("/api/grade")
def grade_answer(request: AnswerRequest):
    answer_text = request.answer.strip()
    word_count = len(answer_text.split())

    # ✅ ให้คะแนนตามความยาวของคำตอบ (เหมาะกับคำตอบสั้น 3–5 บรรทัด)
    if word_count >= 60:
        score = random.randint(85, 100)
        feedback = "คำตอบชัดเจน ครอบคลุมดีมาก"
    elif word_count >= 40:
        score = random.randint(70, 85)
        feedback = "อธิบายได้ดีระดับหนึ่ง เหลือรายละเอียดบางจุด"
    elif word_count >= 20:
        score = random.randint(50, 70)
        feedback = "คำตอบเริ่มมีแนวคิดที่ดี แต่ยังขาดความชัดเจน"
    else:
        score = random.randint(0, 40)
        feedback = "ควรอธิบายให้ชัดเจนมากขึ้น เช่น การทำงานหรือประโยชน์ของ ML"

    # ✅ ส่งผลลัพธ์กลับไปยัง frontend
    return {
        "score": score,
        "similarity": round(similarity, 2),
        "feedback": feedback
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Autograde Backend"}
