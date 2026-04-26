from api_crud_generate_libary.services.service import Service

from src.models import Questions
from src.schemas.questions_schemas import OnlyQuestionsGetSchema

questions_service = Service(Questions)


class QuestionsService:
    @staticmethod
    async def get_last_three_questions(db) -> list:
        """Fetch the last three questions from the database."""
        response = await questions_service.read(
            db=db,
            join_parameters=None,
            second_level_join_parameters=None,
            page=1,
            items_per_page=3,
            direction="desc",
            order_by="created_at",
        )

        if len(response[0]) > 0:
            return [
                OnlyQuestionsGetSchema.model_validate(item)
                for item in response[0]
            ]

        return []
