"""Controller for AI-generated anatomy questions."""

import json
import random

from src.services.ai_anatomy_service import AIAnatomyService
from src.services.questions_service import QuestionsService, questions_service

from src.helpers.questions_text import UBA_DIVERSITY_MODES


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
        last_questions = await QuestionsService.get_last_three_questions(db)
        response = await AIAnatomyService.generate_response(
            parameter, random.choice(UBA_DIVERSITY_MODES), last_questions
        )

        json_response = json.loads(response.output[0].content[0].text)
        json_response["topic"] = parameter

        await questions_service.create(json_response, db)

        return json_response
