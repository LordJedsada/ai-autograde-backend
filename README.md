# AI Autograde API (FastAPI)

ระบบตรวจคำตอบอัตโนมัติด้วย AI สำหรับใช้ร่วมกับ Open edX หรือระบบการเรียนออนไลน์อื่น ๆ

## โครงสร้างระบบ
- Backend: FastAPI
- Embedding Model: SentenceTransformer (BGE-M3)
- Scoring: Cosine Similarity กับ Reference Answer
- Frontend: HTML + JavaScript หรือใช้งานร่วมกับ XML ใน Open edX

## วิธีใช้งาน
1. ติดตั้ง dependencies:
   ```bash
   pip install -r requirements.txt
   
