from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


import pandas as pd
import os
from ..tools.data_tools import get_column_info
from ..agents.titanic_agent import TitanicAgent


router = APIRouter(prefix="/api", tags=["chat"])

# Load Titanic dataset for agent
DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/Titanic-Dataset.csv')
df = pd.read_csv(DATA_PATH)
agent = TitanicAgent(df)


from typing import Optional

class UserQuery(BaseModel):
    question: str
    api_key: Optional[str] = None



@router.get("/columns")
async def columns():
    """Get Titanic dataset column info for testing."""
    return get_column_info()

@router.post("/chat")
async def chat(query: UserQuery):
    """Chat endpoint for Titanic dataset Q&A."""
    try:
        response_dict = agent.process_query(query.question, query.api_key)
        return response_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))