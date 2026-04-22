"""Router for AI anatomy question generation endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.ai_anatomy_controller import AIAnatomyController
from src.schemas.ai_anatomy_schemas import AnatomySchema
from src.configs.db_connection import get_db

ai_anatomy_router = APIRouter()

@ai_anatomy_router.post("/ai")
async def generate_question(data: AnatomySchema, db: AsyncSession = Depends(get_db)):
    """
    Generate an anatomy question using AI.

    Args:
        data: AnatomySchema containing the topic parameter

    Returns:
        dict: Generated question in JSON format
    """
    response = await AIAnatomyController.generate_question(data.parameter, db)
    return response
