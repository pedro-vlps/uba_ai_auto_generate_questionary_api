"""Route declaration module for API endpoints configuration."""

from typing import Any

from src.models.models import (
    Questions,
    Profiles,
    Users,
    Institutions,
    UsersInstitutions,
    QuestionAnswers,
    QuestionFeedbacks,
)
from src.schemas import (
    QuestionsBase,
    QuestionsGet,
    QuestionsPost,
    QuestionsUpdate,
)

from src.configs.db_connection import get_db


routes_declaration: list[dict[str, Any]] = [
    {
        "model_class": Questions,
        "standard_schema": QuestionsBase,
        "db_session": get_db,
        "auth_callback": None,
        "request_post_schema": QuestionsPost,
        "request_update_schema": QuestionsUpdate,
        "response_get_schema": QuestionsGet,
        "response_get_by_id_schema": QuestionsGet,
        "response_post_schema": QuestionsGet,
        "response_delete_schema": None,
        "response_patch_schema": QuestionsGet,
        "enable_get": True,
        "enable_get_by_id": True,
        "enable_post": False,
        "enable_delete": False,
        "enable_patch": False,
        "join_parameters": None,
        "second_level_join_parameters": None,
        "route_prefix": "/questions",
        "route_tags": ["Questions"],
    },
]
