from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.users_controller import UsersController
from src.schemas.users_schemas import UsersPost, UsersNoPasswordResponse
from src.configs.db_connection import get_db

users_router = APIRouter()

@users_router.post("") # , response_model=UsersNoPasswordResponse)
async def create_user(body: UsersPost, db: AsyncSession = Depends(get_db)):
    """Endpoint to create a new user."""
    return await UsersController.create_user(body, db)
