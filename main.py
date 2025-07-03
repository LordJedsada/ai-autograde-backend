from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ควรระบุ URL ของ frontend ใน production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# โหลดโมเดล
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# ฟังก์ชันคำนวณ similarity
def compute_semantic_similarity(student_answer: str, reference_answer: str) -> float:
    embedding1 = model.encode(student_answer, convert_to_tensor=True)
    embedding2 = model.encode(reference_answer, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
    return round(similarity * 100, 2)

class AnswerRequest(BaseModel):
    chapter: int
    question: int
    answer: str

# ✅ สร้าง endpoint สำหรับให้คะแนนคำตอบ
@app.post("/api/grade")
def grade_answer(request: AnswerRequest):
    answer_text = request.answer.strip()
    word_count = len(answer_text.split())

    # สมมุติว่า reference_answer คือตัวคำตอบที่เราจะเปรียบเทียบ
    reference_answer = "คำตอบอ้างอิงของคำถามนี้"

    # คำนวณ similarity
    similarity = compute_semantic_similarity(answer_text, reference_answer)

    # ✅ ให้คะแนนตามความยาวของคำตอบ
    if word_count >= 60:
        score = round(similarity * 10)  # คะแนนตามความคล้ายคลึง
        feedback = "คำตอบชัดเจน ครอบคลุมดีมาก"
    elif word_count >= 40:
        score = round(similarity * 8)
        feedback = "อธิบายได้ดีระดับหนึ่ง เหลือรายละเอียดบางจุด"
    elif word_count >= 20:
        score = round(similarity * 6)
        feedback = "คำตอบเริ่มมีแนวคิดที่ดี แต่ยังขาดความชัดเจน"
    else:
        score = round(similarity * 4)
        feedback = "ควรอธิบายให้ชัดเจนมากขึ้น เช่น การทำงานหรือประโยชน์ของ ML"

    # ✅ ส่งผลลัพธ์กลับไปยัง frontend
    return {
        "score": score,
        "similarity": similarity,
        "feedback": feedback
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Autograde Backend"}
