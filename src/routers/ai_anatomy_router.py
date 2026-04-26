"""Router for AI anatomy question generation endpoints."""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.ai_anatomy_controller import AIAnatomyController
from src.schemas.ai_anatomy_schemas import AnatomySchema
from src.configs.db_connection import get_db

ai_anatomy_router = APIRouter()

@ai_anatomy_router.post("/ai")
async def generate_question(
    request: Request,
    data: AnatomySchema,
    db: AsyncSession = Depends(get_db)
):
    """
    Generate an anatomy question using AI.

    Args:
        request: FastAPI request object
        data: AnatomySchema containing the topic parameter
        db: Database session

    Returns:
        dict: Generated question in JSON format
    """
    institution_id = request.headers.get("x-institution-id")
    response = await AIAnatomyController.generate_question(data.parameter, db, institution_id)
    return response
