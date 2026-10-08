from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/send")
def send_webhook_():
    payload = {
        "username":"Aniket",
        "event":"user created"
    }
    response = requests.post(
        "http://127.0.0.1:8001/webhook",
        json=payload
    )
    return {
        "receiver_response": response.json()
    }