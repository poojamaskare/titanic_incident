# Titanic Chatbot

This project is a chatbot that analyzes the Titanic dataset using FastAPI for the backend, LangChain for the agent framework, and Streamlit for the frontend. The chatbot allows users to ask questions about the Titanic dataset and receive insightful responses based on the analysis of the data.

## Project Structure

```
titanic-chatbot
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── agents
│   │   │   ├── __init__.py
│   │   │   └── titanic_agent.py
│   │   ├── chains
│   │   │   ├── __init__.py
│   │   │   └── analysis_chain.py
│   │   ├── tools
│   │   │   ├── __init__.py
│   │   │   └── data_tools.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── schemas.py
│   │   └── routes
│   │       ├── __init__.py
│   │       └── chat.py
│   ├── data
│   │   └── titanic.csv
│   ├── requirements.txt
│   └── .env.example
├── frontend
│   ├── app.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── chat_interface.py
│   │   └── visualizations.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── api_client.py
│   └── requirements.txt
├── tests
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_routes.py
│   └── test_tools.py
├── .gitignore
├── .env.example
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd titanic-chatbot
   ```

2. Navigate to the backend directory and install the required dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Navigate to the frontend directory and install the required dependencies:
   ```
   cd frontend
   pip install -r requirements.txt
   ```

## Usage

### Backend

1. Start the FastAPI server:
   ```
   cd backend
   uvicorn app.main:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8000`.

### Frontend

1. Start the Streamlit application:
   ```
   cd frontend
   streamlit run app.py
   ```

2. The Streamlit app will be available at `http://localhost:8501`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.