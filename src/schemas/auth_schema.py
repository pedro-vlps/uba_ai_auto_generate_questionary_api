from pydantic import BaseModel

from src.schemas.user_institution_schema import UserInstitutionSchema
from src.schemas.users_schemas import UsersNoPasswordResponse


class LoginSchema(BaseModel):
    """Schema for login credentials."""

    nickname: str
    password: str

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""

        from_attributes = True
        json_schema_extra = {"example": {"nickname": "JokerVLP", "password": "123456"}}


class LoginResponseSchema(BaseModel):
    """Schema for login response with authenticated user data."""

    user: UserInstitutionSchema

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""

        from_attributes = True
        json_schema_extra = {
            "example": {
                "user": {
                    "user": {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "name": "John Doe",
                        "nickname": "johndoe",
                    },
                    "institution": {
                        "id": "123e4567-e89b-12d3-a456-426614174001",
                        "name": "UBA",
                    },
                    "profile": {
                        "id": "123e4567-e89b-12d3-a456-426614174002",
                        "name": "Admin",
                    },
                }
            }
        }


class LoginAdminResponseSchema(BaseModel):
    """Schema for login response with authenticated user data."""

    user: UsersNoPasswordResponse

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""

        from_attributes = True
        json_schema_extra = {
            "example": {
                "user": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "John Doe",
                    "nickname": "johndoe",
                    "global_role": "admin",
                },
            }
        }
