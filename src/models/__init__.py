"""Route declaration module for API endpoints configuration."""
from typing import Any

from src.models.models import Profiles, Questions, Users
from src.schemas import (
    ProfileBase,
    ProfileGet,
    ProfilePost,
    ProfileUpdate,
    QuestionsBase,
    QuestionsGet,
    QuestionsPost,
    QuestionsUpdate,
    UsersBase,
    UsersNoPasswordResponse,
    UsersPost,
    UsersUpdate,
)

from src.configs.db_connection import get_db


routes_declaration: list[dict[str, Any]] = [
    {
        "model_class": Profiles,
        "standard_schema": ProfileBase,
        "db_session": get_db,
        "auth_callback": None,
        "request_post_schema": ProfilePost,
        "request_update_schema": ProfileUpdate,
        "response_get_schema": ProfileGet,
        "response_get_by_id_schema": ProfileGet,
        "response_post_schema": ProfileGet,
        "response_delete_schema": None,
        "response_patch_schema": ProfileGet,
        "enable_get": True,
        "enable_get_by_id": True,
        "enable_post": False,
        "enable_delete": False,
        "enable_patch": False,
        "join_parameters": None,
        "second_level_join_parameters": None,
        "route_prefix": "/profiles",
        "route_tags": ["Profiles"],
    },
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
        "enable_post": True,
        "enable_delete": False,
        "enable_patch": False,
        "join_parameters": None,
        "second_level_join_parameters": None,
        "route_prefix": "/questions",
        "route_tags": ["Questions"],
    },
    {
        "model_class": Users,
        "standard_schema": UsersBase,
        "db_session": get_db,
        "auth_callback": None,
        "request_post_schema": UsersPost,
        "request_update_schema": UsersUpdate,
        "response_get_schema": UsersNoPasswordResponse,
        "response_get_by_id_schema": UsersNoPasswordResponse,
        "response_post_schema": UsersNoPasswordResponse,
        "response_delete_schema": None,
        "response_patch_schema": UsersNoPasswordResponse,
        "enable_get": True,
        "enable_get_by_id": True,
        "enable_post": True,
        "enable_delete": True,
        "enable_patch": True,
        "join_parameters": [
            {
                "model": Profiles,
                "column": "profile_id",
                "response_parameter": Users.profile
            }
        ],
        "second_level_join_parameters": None,
        "route_prefix": "/users",
        "route_tags": ["Users"],
    },
]
