import requests

API_KEY = "sk-ccdb7d4f617c429abea506eab256a7b1"
API_URL = "https://api.deepseek.com/v1/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-coder",
    "prompt": "print('Hello, World!')",
    "temperature": 0.7
}

response = requests.post(API_URL, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
