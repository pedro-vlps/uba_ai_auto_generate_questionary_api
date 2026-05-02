"""Controller for AI-generated anatomy questions."""

import uuid
import json
import random
from fastapi import HTTPException

from src.services.ai_anatomy_service import AIAnatomyService
from src.services.questions_service import QuestionsService, questions_service

from src.helpers.questions_text import UBA_DIVERSITY_MODES
from src.helpers.check_subtopic import check_anatomy_sub_topic


class AIAnatomyController:
    """Controller for handling AI anatomy question generation."""

    @staticmethod
    async def generate_question(parameter: str, db, institution_id):
        """
        Generate an anatomy question using AI based on the specified parameter.

        Args:
            parameter: The anatomy topic parameter (e.g., Neuro, Esplacno, Locomotor)
            institution_id: The institution ID from the request header

        Returns:
            dict: JSON response containing the generated question data
        """

        if institution_id is not None and not isinstance(institution_id, uuid.UUID):
            try:
                institution_id = uuid.UUID(institution_id)
            except ValueError as e:
                raise ValueError(
                    "Invalid institution_id format. Must be a valid UUID."
                ) from e
        else:
            raise HTTPException(
                status_code=400,
                detail="institution_id is required and must be a valid UUID.",
            )

        used_diversity_mode = random.choice(UBA_DIVERSITY_MODES)
        used_subtopic, used_subtopic_description = check_anatomy_sub_topic(parameter)
        used_correct_letter = random.choice(["A", "B", "C", "D"])
        last_questions = await QuestionsService.get_last_three_questions(
            parameter, used_subtopic, db
        )

        response = await AIAnatomyService.generate_response(
            parameter,
            used_subtopic,
            used_subtopic_description,
            used_diversity_mode,
            used_correct_letter,
            last_questions,
        )

        json_response = json.loads(response.output[0].content[0].text)
        json_response["topic"] = parameter
        json_response["subtopic"] = used_subtopic
        json_response["subtopic_description"] = used_subtopic_description
        json_response["diversity_mode"] = used_diversity_mode
        json_response["institution_id"] = institution_id

        question_response = await questions_service.create(json_response, db)

        return {"data": question_response}
