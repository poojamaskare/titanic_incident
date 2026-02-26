def get_api_client():
    import requests

    BASE_URL = "http://localhost:8000"  # Adjust the URL as needed for your backend

    def send_query(query):
        response = requests.post(f"{BASE_URL}/chat", json={"question": query})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get response from the server."}

    return {
        "send_query": send_query
    }