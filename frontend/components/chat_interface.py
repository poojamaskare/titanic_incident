from streamlit import session_state as st_session
import streamlit as st
import requests

class ChatInterface:
    def __init__(self):
        self.api_url = "http://localhost:8000/chat"  # Adjust the URL as needed
        self.user_input = ""
        self.chat_history = []

    def display_chat_interface(self):
        st.title("Titanic Chatbot")
        self.user_input = st.text_input("Ask a question about the Titanic dataset:")
        
        if st.button("Send"):
            self.process_user_input()

        self.display_chat_history()

    def process_user_input(self):
        if self.user_input:
            response = self.get_chatbot_response(self.user_input)
            self.chat_history.append({"user": self.user_input, "bot": response})
            self.user_input = ""

    def get_chatbot_response(self, question):
        try:
            response = requests.post(self.api_url, json={"question": question})
            response.raise_for_status()
            return response.json().get("answer", "Sorry, I didn't understand that.")
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def display_chat_history(self):
        for chat in self.chat_history:
            st.write(f"**You:** {chat['user']}")
            st.write(f"**Bot:** {chat['bot']}")