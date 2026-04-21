from fastapi import APIRouter

from src.controllers.ai_anatomy_controller import AIAnatomyController
from src.schemas.ai_anatomy_schemas import AnatomySchema

ai_anatomy_router = APIRouter()

@ai_anatomy_router.post("/ai")
async def generate_question(data: AnatomySchema):
    response = await AIAnatomyController.generate_question(data.parameter)
    return response
