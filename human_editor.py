import requests

def human_edit(text):
    payload = {
        "model": "llama3",
        "prompt": (
            "You are simulating a professional human editor. "
            "Improve the text below for readability, tone, and smoothness while preserving style and meaning. "
            "Make it feel like it was edited by a human editor, not AI.\n\n"
            f"{text}"
        ),
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)
    data = response.json()

    edited = data.get("response", "").strip()
    return edited + "\n\n🧑 (Human-edited)"
