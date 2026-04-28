from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from src.schemas.profile_schemas import ProfileGet
from src.schemas.institutions_schema import InstitutionGet
from src.schemas.users_schemas import UsersLoginResponse


class UserInstitutionSchema(BaseModel):
    """Schema for user institution association."""

    user_id: UUID
    institution_id: UUID
    profile_id: UUID
    created_at: datetime

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""

        from_attributes = True
        json_schema_extra = {"example": {"token": "token_jwt_aqui"}}


class UserInstitutionSchemaJoin(BaseModel):
    """Schema for user institution association."""

    user: UsersLoginResponse
    institution: InstitutionGet
    profile: ProfileGet

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""

        from_attributes = True
        json_schema_extra = {"example": {"token": "token_jwt_aqui"}}
