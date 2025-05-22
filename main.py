from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = "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"

app = FastAPI()

# Permitir CORS para que el frontend pueda llamar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes limitar aquí el dominio si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat(question: Question):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question.question}]
    )
    answer = response.choices[0].message.content
    return {"answer": answer}
