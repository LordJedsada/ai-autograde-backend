# AI Auto-Grader (FastAPI)

🚀 This Space hosts a FastAPI backend for automatic grading using Hugging Face Inference API.

## Endpoints

- `/api/grade`: Grade a student's answer
- `/api/question`: Retrieve question text

## Environment Variables

Set these in Hugging Face Space "Repository secrets":

- `HF_TOKEN`: Your Hugging Face Inference API Token
- `HF_MODEL`: (default: `google/flan-t5-base`)

## Deploy

1. Clone this repo
2. Create a Hugging Face Space (SDK = Docker)
3. Add secrets under Settings > Repository secrets
4. Done ✅
