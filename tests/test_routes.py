from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={"question": "What was the survival rate?"})
    assert response.status_code == 200
    assert "survival rate" in response.json().get("answer", "")

def test_chat_endpoint_invalid_question():
    response = client.post("/chat", json={"question": ""})
    assert response.status_code == 400
    assert "detail" in response.json()