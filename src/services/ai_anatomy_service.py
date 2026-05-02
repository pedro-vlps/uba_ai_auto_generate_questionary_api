"""Service for AI-generated anatomy questions using OpenAI."""

from openai import OpenAI

from src.helpers.questions_text import ANATOMY_QUESTION

client = OpenAI()


class AIAnatomyService:
    """Service for generating anatomy questions using AI."""

    @staticmethod
    async def generate_response(
        parameter: str,
        subtopic: str,
        diversity_mode: str,
        recent_questions: list,
    ):
        """
        Generate an AI response for an anatomy question.

        Args:
            parameter: The anatomy topic parameter to include in the prompt
            diversity_mode: The mode for generating diverse questions
            recent_questions: A list of recently generated questions to avoid repetition
        Returns:
            Response: OpenAI response object containing the generated question
        """
        # Format the prompt with the topic
        formatted_question = ANATOMY_QUESTION.replace("{TOPIC}", parameter)

        formatted_question = ANATOMY_QUESTION.replace("{SUB_TOPIC}", subtopic)

        formatted_question = formatted_question.replace(
            "{DIVERSITY_MODE}", diversity_mode
        )

        if recent_questions:
            formatted_question = formatted_question.replace(
                "{RECENT_QUESTIONS}",
                "\n".join(item.question for item in recent_questions),
            )
        else:
            formatted_question = formatted_question.replace(
                "{RECENT_QUESTIONS}",
                "There are no recent questions to avoid repetition.",
            )

        # Use the AI model to generate a response based on the prompt
        response = client.responses.create(
            model="gpt-5.4-mini", input=formatted_question
        )

        return response
