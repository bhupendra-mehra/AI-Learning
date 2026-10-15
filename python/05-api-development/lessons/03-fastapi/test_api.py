import requests

BASE_URL = "http://127.0.0.1:8000"

payload = {
    "name": "Priya Patel",
    "email": "priya@example.com",
    "age": 24,
}

response = requests.post(
    f"{BASE_URL}/students",
    json=payload,
    timeout=10,
)

print("Status Code:", response.status_code)
print("Response:", response.text)

if response.ok:
    print("Student created:", response.json())
