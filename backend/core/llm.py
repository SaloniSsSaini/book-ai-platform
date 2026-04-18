import requests

def query_llm(prompt):
    res = requests.post(
        "http://localhost:1234/v1/chat/completions",
        json={
            "model": "local-model",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return res.json()['choices'][0]['message']['content']