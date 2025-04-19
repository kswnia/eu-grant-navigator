import requests

def ask_ollama(prompt, model="mistral"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code != 200:
        raise Exception(f"Ollama failed: {response.text}")
    return response.json()["response"].strip()
