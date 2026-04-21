"""Controller for AI-generated anatomy questions."""
import json
from src.services.ai_anatomy_service import AIAnatomyService

class AIAnatomyController:
    """Controller for handling AI anatomy question generation."""

    @staticmethod
    async def generate_question(parameter: str):
        """
        Generate an anatomy question using AI based on the specified parameter.

        Args:
            parameter: The anatomy topic parameter (e.g., Neuro, Esplacno, Locomotor)

        Returns:
            dict: JSON response containing the generated question data
        """
        response = await AIAnatomyService.generate_response(parameter)

        json_response = json.loads(response.output[0].content[0].text)

        return json_response
