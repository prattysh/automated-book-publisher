import requests

def ai_reviewer(text):
    payload = {
        "model": "llama3",
        "prompt": f"Polish the following text for grammar, clarity, and formatting, keeping the meaning unchanged:\n\n{text}",
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    data = response.json()

    reviewed = data.get("response", "").strip()
    return reviewed + "\n\n✅ (Polished by AI Reviewer)"
