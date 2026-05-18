import ollama
from app.core.config import OLLAMA_MODEL


def generate(prompt: str):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
