from sentence_transformers import SentenceTransformer, util
from grading.answer_data import reference_answers

# โหลดโมเดลฝึกจากหลายภาษา (รองรับคำตอบภาษาไทย)
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def compute_semantic_similarity(student_answer: str, reference_answer: str) -> float:
    embedding1 = model.encode(student_answer, convert_to_tensor=True)
    embedding2 = model.encode(reference_answer, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
    return round(similarity * 100, 2)  # คืนค่า similarity เป็นเปอร์เซ็นต์

def grade_answer(chapter: int, question: int, answer_text: str):
    ideal = reference_answers.get(chapter, {}).get(question)
    if not ideal:
        return {"score": 0, "similarity": 0, "feedback": "ไม่พบคำตอบอ้างอิงในระบบ กรุณาตรวจสอบเลขบทหรือคำถาม"}

    similarity = compute_semantic_similarity(answer_text, ideal)
    score = similarity  # ในที่นี้ใช้ similarity เป็นคะแนนโดยตรง

    # Feedback ตามช่วงคะแนน
    if score >= 90:
        feedback = "ดีมาก — อธิบายได้ครบถ้วนและชัดเจน"
    elif score >= 80:
        feedback = "ดี — มีความเข้าใจที่ดีแต่ยังพัฒนาได้อีก"
    elif score >= 60:
        feedback = "กลาง — มีบางส่วนที่ยังขาดหายหรือคลุมเครือ"
    elif score >= 40:
        feedback = "ต่ำ — ควรเสริมรายละเอียดให้ชัดเจนขึ้น"
    else:
        feedback = "ควรปรับปรุง — คำตอบยังไม่ตรงประเด็น"

    return {
        "score": score,
        "similarity": similarity,
        "feedback": feedback
    }

