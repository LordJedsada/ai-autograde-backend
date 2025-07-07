from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from grading.grader import grade
from grading.question_data import questions  # ✅ เพิ่มเพื่อใช้ดึงคำถาม

app = FastAPI()

# ✅ เพิ่ม CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # แนะนำระบุ origin จริงใน production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ โมเดลสำหรับรับคำตอบ
class AnswerRequest(BaseModel):
    chapter: int
    question: int
    answer: str

# ✅ โมเดลสำหรับขอดึงคำถาม
class QuestionRequest(BaseModel):
    chapter: int
    question: int

# ✅ Endpoint สำหรับให้คะแนน
@app.post("/api/grade")
def grade_answer(request: AnswerRequest):
    return grade(
        chapter=request.chapter,
        question=request.question,
        student_answer=request.answer
    )

# ✅ Endpoint สำหรับแสดงคำถาม
@app.post("/api/question")
def get_question(request: QuestionRequest):
    key = f"{request.chapter}_{request.question}"
    q = questions.get(request.chapter, {}).get(key)
    return {
        "question": q or "❌ ไม่พบคำถามในบทที่นี้"
    }
