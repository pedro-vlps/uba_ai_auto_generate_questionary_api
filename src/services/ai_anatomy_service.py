from openai import OpenAI

from src.helpers.questions_text import anatomy_question

client = OpenAI()

class AIAnatomyService:
    @staticmethod
    async def generate_response(parameter: str):
        # Format the prompt with the topic
        formatted_question = anatomy_question.replace("{TOPIC}", parameter)
        # Use the AI model to generate a response based on the prompt
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=formatted_question
        )
        return response
