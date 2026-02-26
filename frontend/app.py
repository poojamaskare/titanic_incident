import streamlit as st
import base64
import pandas as pd
import os
import sys

# Add the parent directory to Python path to ensure absolute import works
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.visualizations import plot_survival_rate, plot_age_distribution, plot_class_distribution

# Add frontend directory to path so logic.py can be imported easily
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logic import TitanicAgent

@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # If starting from root, base_dir is root.
    # The dataset lives in root/backend/data/Titanic-Dataset.csv
    file_path = os.path.join(base_dir, "backend", "data", "Titanic-Dataset.csv")
    if not os.path.exists(file_path):
        # Fallback if the folder structure changes slightly
        file_path = "backend/data/Titanic-Dataset.csv"
    return pd.read_csv(file_path)

@st.cache_resource
def get_agent(_data):
    return TitanicAgent(_data)

def main():
    st.title("Titanic Chatbot")
    st.write("Ask me anything about the Titanic dataset!")

    try:
        data = load_data()
        agent = get_agent(data)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return

    user_input = st.text_input("Your question:")
    
    if st.button("Submit"):
        if user_input:
            with st.spinner("Thinking..."):
                try:
                    resp_data = agent.process_query(user_input)
                    answer = resp_data.get("answer")
                    if answer:
                        st.write(f"**Bot:** {answer}")
                    else:
                        st.write("**Bot:** I don't know the answer to that.")
                    
                    image_b64 = resp_data.get("image")
                    if image_b64:
                        try:
                            image_bytes = base64.b64decode(image_b64)
                            st.image(image_bytes, caption="Generated Visualization")
                        except Exception as e:
                            st.error(f"Failed to display image: {e}")
                except Exception as e:
                    st.error(f"An error occurred while processing: {e}")
        else:
            st.write("Please enter a question.")
    

    st.write("---")
    st.subheader("Data Visualizations")
    col1, col2, col3 = st.columns(3)
    
    if col1.button("Survival Rate"):
        plot_survival_rate(data)
        
    if col2.button("Age Distribution"):
        plot_age_distribution(data)
        
    if col3.button("Class Distribution"):
        plot_class_distribution(data)

if __name__ == "__main__":
    main()