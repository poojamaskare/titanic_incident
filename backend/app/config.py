from pydantic import BaseSettings

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Titanic Chatbot"
    VERSION: str = "1.0.0"
    
    # Database settings (if applicable)
    DATABASE_URL: str = "sqlite:///./titanic.db"
    
    # API settings
    API_PREFIX: str = "/api"
    
    class Config:
        env_file = ".env"

settings = Settings()