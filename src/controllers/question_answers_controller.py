"""Question Answers Controller"""

from uuid import UUID

from src.services.question_answers_service import QuestionAnswersService


class QuestionAnswersController:
    """Controller for handling question answer operations."""

    @staticmethod
    async def get_questions_with_latest_user_answers(
        user_id: UUID,
        db,
    ):
        """Return all questions with the latest answer sent by the given user, if any."""
        response = await QuestionAnswersService.get_questions_with_latest_user_answers(
            user_id,
            db,
        )
        return response
