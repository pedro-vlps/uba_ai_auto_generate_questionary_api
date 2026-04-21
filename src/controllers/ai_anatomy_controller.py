from src.services.ai_anatomy_service import AIAnatomyService

class AIAnatomyController:
    @staticmethod
    async def generate_question(parameter: str):
        response = await AIAnatomyService.generate_response(parameter)
        return response
