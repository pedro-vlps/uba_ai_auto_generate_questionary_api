from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.db_connection import get_db
from src.controllers.question_answers_controller import QuestionAnswersController

question_answers_router = APIRouter()


@question_answers_router.get("/latest-answers")
async def get_questions_with_latest_user_answers(
    user_id: str,
    db: AsyncSession = Depends(get_db),
):
    """
    Return all questions with the latest answer sent by the given user, if any.

    Args:
        user_id: The ID of the user to filter answers by
        db: Database session dependency

    Returns:
        A list of questions with the latest answer from the specified user, if any.
    """
    response = await QuestionAnswersController.get_questions_with_latest_user_answers(
        user_id,
        db,
    )
    return response
