import requests
import json

def ai_writer(text):
    payload = {
        "model": "llama3",
        "prompt": f"Rewrite this in modern, smooth, and polished English:\n\n{text}",
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    data = response.json()

    rewritten = data.get("response", "").strip()
    return rewritten + "\n\n📝 (Spun by AI Writer)"
