"""Authentication router for login endpoints."""

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.auth_controller import AuthController
from src.schemas.auth_schema import (
    LoginSchema,
    LoginResponseSchema,
    LoginAdminResponseSchema,
)
from src.configs.db_connection import get_db

auth_router = APIRouter()


@auth_router.post(
    "/login", response_model=LoginResponseSchema | LoginAdminResponseSchema
)
async def login(
    request: Request, body: LoginSchema, db: AsyncSession = Depends(get_db)
):
    """
    Handle user login request.

    Args:
        request: Current HTTP request used to store auth cookie state
        body: Login credentials containing nickname and password
        db: Database session dependency

    Returns:
        LoginResponseSchema: JWT token response
    """
    response, token = await AuthController.login(body.nickname, body.password, db)
    request.state.auth_token = token
    return response
