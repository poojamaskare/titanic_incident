# backend/app/__init__.py

from fastapi import FastAPI

app = FastAPI()

from .routes import chat

app.include_router(chat.router)