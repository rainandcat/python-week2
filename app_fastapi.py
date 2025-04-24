from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="grok-3-beta",
            messages=[
                {"role": "system", "content": "You are Grok, a highly intelligent, helpful AI assistant."},
                {"role": "user", "content": req.message}
            ],
            max_tokens=150,
            temperature=0.7,
            stream=False
        )
        reply = response.choices[0].message.content.strip()
        return {"reply": reply}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
