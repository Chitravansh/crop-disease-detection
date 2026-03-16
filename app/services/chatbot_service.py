import os
from openai import OpenAI
from flask import session

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def ask_chatbot(message, history):

    language = session.get("language", "en")

    language_map = {
        "en": "English",
        "hi": "Hindi",
        "mr": "Marathi",
        "pa": "Punjabi"
    }

    response_language = language_map.get(language, "English")

    system_prompt = f"""
You are an agricultural expert assisting farmers using the ArogyaFasal platform.

Your answers must follow this structure:

### 🌿 Problem
Short explanation of the issue.

### 🔍 Possible Causes
- cause 1
- cause 2
- cause 3

### 🛠 Recommended Treatment
- treatment 1
- treatment 2

### 🌱 Prevention Tips
- tip 1
- tip 2

Use simple language farmers can understand.

Respond in {response_language}.
"""

    messages = [{"role": "system", "content": system_prompt}] + history + [
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.4,
    )

    return response.choices[0].message.content