"""Main API File"""
from fastapi import FastAPI

from src.routers import ai_anatomy_router

app = FastAPI()

@app.get("/healthy")
def healthy():
    """Healthy check route"""
    return { "status": "Ok" }

app.include_router(
    ai_anatomy_router,
    prefix="/anatomy",
    tags=["Anatomy"]
)
