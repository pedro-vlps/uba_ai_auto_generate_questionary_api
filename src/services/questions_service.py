from api_crud_generate_libary.services.service import Service

from src.models import Questions

questions_service = Service(Questions)


class QuestionsService:
    @staticmethod
    async def get_last_three_questions(db):
        """Fetch the last three questions from the database."""
        return await questions_service.read(
            db=db,
            join_parameters=None,
            second_level_join_parameters=None,
            page=1,
            items_per_page=3,
            direction="desc",
            order_by="created_at",
        )
