from typing import Optional
from uuid import UUID

from pydantic import BaseModel, field_validator
from cryptography.fernet import Fernet

from src.schemas.profile_schemas import ProfileGet
from src.configs.configs import settings


class UsersBase(BaseModel):
    nickname: str
    password: str
    profile_id: Optional[UUID] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "nickname": "johndoe",
                "password": "securepassword123",
                "profile_id": "123e4567-e89b-12d3-a456-426614174000",
            }
        }


class UsersUpdate(BaseModel):
    nickname: Optional[str] = None
    password: Optional[str] = None
    profile_id: Optional[UUID] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {"nickname": "janedoe", "password": "newpassword456"}
        }

    @field_validator("nickname", "password", mode="before")
    @classmethod
    def encrypt_fields(cls, value: str) -> str:
        """Criptografa nickname e password antes de salvar"""
        if not value:
            return value
        cipher = Fernet(settings.FERNET_KEY.encode())
        return cipher.encrypt(value.encode()).decode()


class UsersPost(UsersBase):
    @field_validator("nickname", "password", mode="before")
    @classmethod
    def encrypt_fields(cls, value: str) -> str:
        """Criptografa nickname e password antes de salvar"""
        if not value:
            return value
        cipher = Fernet(settings.FERNET_KEY.encode())
        return cipher.encrypt(value.encode()).decode()


class UsersGet(UsersBase):
    id: UUID
    profile: Optional[ProfileGet] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "nickname": "johndoe",
                "password": "securepassword123",
                "profile_id": "123e4567-e89b-12d3-a456-426614174000",
                "profile": {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "Admin",
                    "counter_limit": 100,
                },
            }
        }

    @field_validator("nickname", "password", mode="after")
    @classmethod
    def decrypt_fields(cls, value: str) -> str:
        """Descriptografa nickname e password após carregar do banco"""
        if not value:
            return value
        try:
            cipher = Fernet(settings.FERNET_KEY.encode())
            return cipher.decrypt(value.encode()).decode()
        except Exception: # pylint: disable=broad-exception-caught
            return value
