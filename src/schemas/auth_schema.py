from pydantic import BaseModel

from src.schemas.user_institution_schema import UserInstitutionSchema


class LoginSchema(BaseModel):
    """Schema for login credentials."""

    nickname: str
    password: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""

        from_attributes = True
        json_schema_extra = {"example": {"nickname": "JokerVLP", "password": "123456"}}


class LoginResponseSchema(BaseModel):
    """Schema for login response with JWT token."""

    token: str
    user: UserInstitutionSchema

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {"example": {"token": "token_jwt_aqui"}}
