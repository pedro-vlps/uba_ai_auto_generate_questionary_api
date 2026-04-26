"""Service for AI-generated anatomy questions using OpenAI."""
import json
from openai import OpenAI

from src.helpers.questions_text import ANATOMY_QUESTION

client = OpenAI()


class AIAnatomyService:
    """Service for generating anatomy questions using AI."""

    @staticmethod
    async def generate_response(
        parameter: str,
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

        # print(formatted_question)

        # Use the AI model to generate a response based on the prompt
        # response = client.responses.create(
        #     model="gpt-4.1-mini", input=formatted_question
        # )

        json_response = json.dumps(
            {
              "question": "Un paciente presenta ictericia y dolor en el cuadrante superior derecho tras una cirugía de urgencia abdominal. Se sospecha una lesión en la vía biliar. ¿Cuál de las siguientes estructuras es más probable que haya resultado lesionada y afecta el drenaje biliar hacia el duodeno?",
              "answer_a": "Conducto hepático común",
              "answer_b": "Conducto pancreático principal",
              "answer_c": "Conducto colédoco",
              "answer_d": "Conducto cístico",
              "explanation_a": "El conducto hepático común recoge la bilis del hígado pero se une al cístico para formar el colédoco.",
              "explanation_b": "El conducto pancreático transporta enzimas pancreáticas, no bilis, por lo que no causa ictericia directa.",
              "explanation_c": "El conducto colédoco lleva la bilis hacia el duodeno; su lesión produce estasis biliar y ictericia.",
              "explanation_d": "El conducto cístico conecta la vesícula con el colédoco; su lesión puede afectar la vesícula pero menos la ictericia.",
              "correct_answer": "C",
              "topic": "Esplacno",
              "subject": "conceptual_reasoning"
            }
        )
        return {
            "output":[
                {
                    "content":[
                        {
                            "text": json_response
                        }
                    ]
                }
            ]
        }
