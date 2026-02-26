import streamlit as st
import requests
import base64
import pandas as pd
import os
import sys

# Add the parent directory to Python path to ensure absolute import works
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.visualizations import plot_survival_rate, plot_age_distribution, plot_class_distribution

API_URL = "http://localhost:8000/api/chat"

@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return pd.read_csv(os.path.join(base_dir, "backend", "data", "Titanic-Dataset.csv"))

def main():
    st.title("Titanic Chatbot")
    st.write("Ask me anything about the Titanic dataset!")

    user_input = st.text_input("Your question:")
    
    if st.button("Submit"):
        if user_input:
            response = requests.post(API_URL, json={"question": user_input})
            if response.status_code == 200:
                resp_data = response.json()
                answer = resp_data.get("answer")
                st.write(f"**Bot:** {answer}")
                
                image_b64 = resp_data.get("image")
                if image_b64:
                    try:
                        image_bytes = base64.b64decode(image_b64)
                        st.image(image_bytes, caption="Generated Visualization")
                    except Exception as e:
                        st.error(f"Failed to display image: {e}")
            else:
                st.write("Error: Unable to get a response from the server.")
        else:
            st.write("Please enter a question.")
    


    st.write("---")
    st.subheader("Data Visualizations")
    col1, col2, col3 = st.columns(3)
    
    data = load_data()
    
    if col1.button("Survival Rate"):
        plot_survival_rate(data)
        
    if col2.button("Age Distribution"):
        plot_age_distribution(data)
        
    if col3.button("Class Distribution"):
        plot_class_distribution(data)

if __name__ == "__main__":
    main()