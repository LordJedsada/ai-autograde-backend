import os
import json
import requests
from dotenv import load_dotenv
from grading.question_data import questions

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "google/flan-t5-base")

def grade(chapter: int, question: int, student_answer: str):
    key = f"{chapter}_{question}"
    question_text = questions.get(chapter, {}).get(key, {}).get("question", "")
    reference_answer = questions.get(chapter, {}).get(key, {}).get("answer", "")

    if not question_text or not reference_answer:
        return {"error": "❌ ไม่พบคำถามหรือคำตอบอ้างอิง"}

    prompt = f"""
You are an AI grader.

Question: {question_text}
Reference Answer: {reference_answer}
Student Answer: {student_answer}

Give score (0-10) and brief feedback in JSON format like:
{{"score": 8, "feedback": "Good explanation but lacks detail."}}
"""

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

    try:
        response = requests.post(url, headers=headers, json={"inputs": prompt})
        result = response.json()
        raw_text = result[0]["generated_text"]

        try:
            feedback_json = json.loads(raw_text)
        except json.JSONDecodeError:
            return {
                "question": question_text,
                "reference_answer": reference_answer,
                "student_answer": student_answer,
                "score": 0,
                "feedback": "⚠️ Model did not return valid JSON: " + raw_text
            }

        return {
            "question": question_text,
            "reference_answer": reference_answer,
            "student_answer": student_answer,
            "score": feedback_json.get("score", 0),
            "feedback": feedback_json.get("feedback", "No feedback returned.")
        }

    except Exception as e:
        return {"error": str(e)}
