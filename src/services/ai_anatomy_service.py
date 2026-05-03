"""Service for AI-generated anatomy questions using OpenAI."""

from openai import OpenAI

from src.helpers.questions_text import get_anatomy_question_prompt

client = OpenAI()


class AIAnatomyService:
    """Service for generating anatomy questions using AI."""

    @staticmethod
    async def generate_response(
        parameter: str,
        subtopic: str,
        subtopic_description: str,
        diversity_mode: str,
        correct_letter: str,
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
        formatted_question = get_anatomy_question_prompt(parameter)

        if recent_questions:
            recent_questions_text = "\n".join(
                item.question for item in recent_questions
            )
        else:
            recent_questions_text = "There are no recent questions to avoid repetition."

        prompt_variables = {
            "{TOPIC}": parameter,
            "{SUB_TOPIC}": subtopic,
            "{SUBTOPIC_DESCRIPTION}": subtopic_description,
            "{CORRECT_LETTER}": correct_letter,
            "{DIVERSITY_MODE}": diversity_mode,
            "{RECENT_QUESTIONS}": recent_questions_text,
        }

        for placeholder, value in prompt_variables.items():
            formatted_question = formatted_question.replace(placeholder, value)

        # Use the AI model to generate a response based on the prompt
        response = client.responses.create(
            model="gpt-5.4-mini", input=formatted_question
        )

        return response
