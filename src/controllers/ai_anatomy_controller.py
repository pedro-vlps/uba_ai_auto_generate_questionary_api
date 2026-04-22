"""Controller for AI-generated anatomy questions."""
import json
from api_crud_generate_libary.services.service import Service

from src.services.ai_anatomy_service import AIAnatomyService
from src.models import Questions

questions_service = Service(Questions)


class AIAnatomyController:
    """Controller for handling AI anatomy question generation."""

    @staticmethod
    async def generate_question(parameter: str, db):
        """
        Generate an anatomy question using AI based on the specified parameter.

        Args:
            parameter: The anatomy topic parameter (e.g., Neuro, Esplacno, Locomotor)

        Returns:
            dict: JSON response containing the generated question data
        """
        response = await AIAnatomyService.generate_response(parameter)

        json_response = json.loads(response.output[0].content[0].text)

        await questions_service.create(json_response, db)

        return json_response
