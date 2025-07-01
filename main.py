from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()

# ✅ เปิด CORS ให้ frontend เข้าถึง
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ โหลด embedding model (รองรับภาษาไทยด้วย!)
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# ✅ โจทย์และคำเฉลยตัวอย่าง (ย่อให้สั้น — สามารถเพิ่มเต็มได้)
reference_answers = {
    1: {
        1: "AI คือศาสตร์ที่ทำให้เครื่องมีความฉลาด ส่วน ML เป็นส่วนหนึ่งของ AI ที่เรียนรู้จากข้อมูล และ DL เป็น ML ที่ใช้โครงข่ายประสาทเทียมที่มีหลายชั้น",
        2: "Machine Learning แบ่งเป็น Supervised Learning ที่มีคำตอบ, Unsupervised Learning ที่ไม่มีคำตอบ และ Reinforcement Learning ที่เรียนรู้ผ่านการลองผิดลองถูก",
        3: "Deep Learning ใช้โครงข่ายประสาทเทียมที่มีหลายชั้นในการประมวลผลข้อมูล ทำให้สามารถเรียนรู้จากภาพและเสียงได้อย่างมีประสิทธิภาพ",
        4: "ข้อมูลมีบทบาทสำคัญในการฝึก AI หากข้อมูลไม่ดี เช่น ข้อมูลผิดพลาดหรือมีอคติ อาจทำให้ผลลัพธ์ที่ได้ไม่แม่นยำ",
        5: "โครงข่ายประสาทเทียมเลียนแบบการทำงานของสมองมนุษย์ โดยมี neuron ที่เชื่อมโยงกันผ่าน synapse และส่งข้อมูลแบบลำดับขั้น",
        6: "AI สามารถทำงานที่ต้องใช้ความแม่นยำสูง เช่น การวิเคราะห์ภาพทางการแพทย์ได้ดีกว่ามนุษย์ แต่ยังไม่สามารถทำงานที่ต้องใช้อารมณ์หรือความเห็นอกเห็นใจได้",
        7: "AI มีผลดีต่อสังคม เช่น เพิ่มประสิทธิภาพในการทำงาน แต่ก็อาจสร้างผลเสีย เช่น การแทนที่แรงงานมนุษย์และปัญหาความเป็นส่วนตัว",
        8: "ผู้เริ่มต้นควรเริ่มจากเรียนรู้พื้นฐานของ Python, คณิตศาสตร์เบื้องต้น จากนั้นศึกษาหลักการของ AI, ML และ DL ตามลำดับ",
        9: "AI อาจแทนที่บางงานของมนุษย์ในอนาคต แต่ยังมีข้อจำกัดทางด้านจริยธรรม เทคโนโลยี และความซับซ้อนของสังคมที่ทำให้แทนที่ทั้งหมดได้ยาก",
        10: "AI ถูกใช้งานในชีวิตประจำวัน เช่น Google Assistant หรือการแนะนำสินค้า ซึ่งช่วยให้ผู้ใช้สะดวกขึ้นและตัดสินใจได้ง่ายขึ้น"
    }
}


# ✅ ข้อมูลจากผู้ใช้
class AnswerRequest(BaseModel):
    chapter: int
    question: int
    answer: str

@app.post("/api/grade")
def grade_answer(req: AnswerRequest):
    ch = req.chapter
    qn = req.question
    user_answer = req.answer.strip()

    ref_answer = reference_answers.get(ch, {}).get(qn)
    if not ref_answer:
        return {
            "score": 0,
            "feedback": f"ยังไม่มีเฉลยสำหรับบทที่ {ch} ข้อ {qn}"
        }

    emb_ref = model.encode(ref_answer, convert_to_tensor=True)
    emb_user = model.encode(user_answer, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(emb_ref, emb_user).item()
    score = round(similarity * 10)

    return {
        "score": score,
        "similarity": round(similarity, 2),
        "feedback": f"ระดับความใกล้เคียง: {round(similarity * 100)}%"
    }
