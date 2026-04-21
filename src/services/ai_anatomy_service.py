"""Service for AI-generated anatomy questions using OpenAI."""
from openai import OpenAI

from src.helpers.questions_text import ANATOMY_QUESTION

client = OpenAI()

class AIAnatomyService:
    """Service for generating anatomy questions using AI."""

    @staticmethod
    async def generate_response(parameter: str):
        """
        Generate an AI response for an anatomy question.

        Args:
            parameter: The anatomy topic parameter to include in the prompt

        Returns:
            Response: OpenAI response object containing the generated question
        """
        # Format the prompt with the topic
        formatted_question = ANATOMY_QUESTION.replace("{TOPIC}", parameter)
        # Use the AI model to generate a response based on the prompt
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=formatted_question
        )
        return response
