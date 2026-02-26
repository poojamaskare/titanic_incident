from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.agents.titanic_agent import TitanicAgent

client = TestClient(app)

def test_titanic_agent_process_query():
    agent = TitanicAgent()
    query = "What was the survival rate of passengers?"
    response = agent.process_query(query)
    assert response is not None
    assert "survival rate" in response.lower()

def test_titanic_agent_invalid_query():
    agent = TitanicAgent()
    query = "This is an invalid query."
    response = agent.process_query(query)
    assert response is None or "I don't understand" in response.lower()

def test_api_titanic_agent():
    response = client.post("/chat", json={"question": "What was the survival rate of passengers?"})
    assert response.status_code == 200
    assert "survival rate" in response.json().get("answer").lower()

def test_api_invalid_query():
    response = client.post("/chat", json={"question": "This is an invalid query."})
    assert response.status_code == 200
    assert "I don't understand" in response.json().get("answer").lower()