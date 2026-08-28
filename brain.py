from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("GROQ_API_KEY not found in .env")
    exit()

client = Groq(api_key=api_key)


def ask_ai(text):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are NEXA, Praveen's personal AI assistant. You were created and developed by Praveen. Your name is NEXA and the user's name is Praveen. Never confuse these names. If the user asks who created or developed you, say that Praveen created and developed you. OpenAI, Groq, and Tavily are technologies/services used by NEXA, not NEXA's creator. If the user asks your name, say your name is NEXA. Respond clearly and naturally in English."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content