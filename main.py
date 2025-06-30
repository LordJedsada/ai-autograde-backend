from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

# ✅ เพิ่มสำหรับ semantic similarity
from sentence_transformers import SentenceTransformer, util

# ✅ โหลดโมเดล
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Ideal answer สำหรับวัด semantic similarity
IDEAL_ANSWER = """
Machine Learning คือกระบวนการที่ทำให้คอมพิวเตอร์สามารถเรียนรู้จากข้อมูล 
โดยไม่ต้องมีการเขียนโปรแกรมใหม่สำหรับทุกกรณี มันเป็นสาขาย่อยของปัญญาประดิษฐ์ 
ที่เน้นการพัฒนาอัลกอริธึมเพื่อให้ระบบสามารถวิเคราะห์และตัดสินใจได้จากข้อมูลที่ได้รับ
"""

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

@app.post("/api/grade")
def grade_answer(request: AnswerRequest):
    answer_text = request.answer.strip()
    word_count = len(answer_text.split())

    # ✅ วัด semantic similarity
    student_vec = model.encode(answer_text, convert_to_tensor=True)
    ideal_vec = model.encode(IDEAL_ANSWER, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(student_vec, ideal_vec).item()

    # ✅ ใช้เกณฑ์ "นับจำนวนคำ" เหมือนเดิมในการให้คะแนน
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

    return {
        "score": score,
        "feedback": feedback,
        "similarity": round(similarity, 3),
        "word_count": word_count
    }

# ✅ route ทดสอบ
@app.get("/")
def read_root():
    return {"message": "👋 Welcome to the AI Autograde Backend!"}
