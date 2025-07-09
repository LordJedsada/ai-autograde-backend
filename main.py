from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from grading.grader import grade  # ใช้ grader ที่ตาเขียน
from grading.question_data import questions  # ใช้แสดงคำถาม

app = FastAPI()

# ✅ เพิ่ม CORS Middleware (เพื่อให้เรียก API จาก frontend ได้)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # เปลี่ยนเป็น origin จริงใน production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ รับข้อมูลคำตอบจากผู้ใช้
class AnswerRequest(BaseModel):
    chapter: int
    question: int
    answer: str

# ✅ ใช้ขอคำถามไปแสดงใน frontend
class QuestionRequest(BaseModel):
    chapter: int
    question: int

# ✅ Endpoint สำหรับประเมินคำตอบ
@app.post("/api/grade")
def grade_answer(request: AnswerRequest):
    return grade(
        chapter=request.chapter,
        question=request.question,
        student_answer=request.answer
    )

# ✅ Endpoint สำหรับดึงคำถามตามบทและข้อ
@app.post("/api/question")
def get_question(request: QuestionRequest):
    key = f"{request.chapter}_{request.question}"
    q = questions.get(request.chapter, {}).get(key)
    return {
        "question": q or "❌ ไม่พบคำถามในบทที่นี้"
    }
