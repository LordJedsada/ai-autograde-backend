# grader.py
from sentence_transformers import SentenceTransformer, util
from grading.answer_data import reference_answers
from grading.question_data import questions  # ✅ เพิ่ม

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def grade(chapter: int, question: int, student_answer: str) -> dict:
    student_answer = student_answer.strip()
    reference_answer = reference_answers.get(chapter, {}).get(question)

    question_key = f"{chapter}_{question}"
    question_text = questions.get(chapter, {}).get(question_key, "❓ ไม่พบคำถามในระบบ")

    if reference_answer is None:
        return {
            "score": 0,
            "similarity": 0.0,
            "feedback": f"❌ ไม่พบคำตอบอ้างอิงในบทที่ {chapter} ข้อที่ {question}",
            "question": question_text
        }

    embedding1 = model.encode(student_answer, convert_to_tensor=True)
    embedding2 = model.encode(reference_answer, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
    score = round(similarity * 100, 2)

    if score > 70:
        feedback = "✅ ดีมาก อธิบายได้ชัดเจน"
    elif score > 50:
        feedback = "📝 พอใช้ ควรอธิบายให้ชัดเจนขึ้น"
    else:
        feedback = "❌ ควรปรับปรุงคำตอบให้สอดคล้องกับคำถาม"

    return {
        "score": score,
        "similarity": score,
        "feedback": feedback,
        "question": question_text  # ✅ เพิ่มบรรทัดนี้
    }
