from pydantic import BaseModel
from typing import List, Optional

class PassengerSchema(BaseModel):
    passenger_id: int
    survived: int
    pclass: int
    name: str
    sex: str
    age: Optional[float]
    sibsp: int
    parch: int
    ticket: str
    fare: float
    cabin: Optional[str]
    embarked: str

class AnalysisRequestSchema(BaseModel):
    question: str
    filters: Optional[dict] = None

class AnalysisResponseSchema(BaseModel):
    answer: str
    details: Optional[dict] = None

class SummarySchema(BaseModel):
    total_passengers: int
    survived_count: int
    survival_rate: float
    average_fare: float
    class_distribution: List[dict]