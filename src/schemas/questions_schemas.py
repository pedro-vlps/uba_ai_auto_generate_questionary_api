"""Pydantic schemas for question data validation and serialization."""
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class QuestionsBase(BaseModel):
    """Base schema for multiple-choice question data."""
    pergunta: str
    resposta_a: str
    resposta_b: str
    resposta_c: str
    resposta_d: str
    resposta_certa: str
    questao_completa: str
    explicacao_a: Optional[str] = None
    explicacao_b: Optional[str] = None
    explicacao_c: Optional[str] = None
    explicacao_d: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "pergunta": "Qual é a capital do Brasil?",
                "resposta_a": "São Paulo",
                "resposta_b": "Rio de Janeiro",
                "resposta_c": "Brasília",
                "resposta_d": "Belo Horizonte",
                "resposta_certa": "C",
                "questao_completa": "Pergunta: Qual é a capital do Brasil?\nA) São Paulo\nB) Rio de Janeiro\nC) Brasília\nD) Belo Horizonte",
                "explicacao_a": "São Paulo é a maior cidade, mas não a capital.",
                "explicacao_b": "Rio de Janeiro foi a capital antiga.",
                "explicacao_c": "Brasília é a capital atual.",
                "explicacao_d": "Belo Horizonte é uma cidade importante, mas não a capital."
            }
        }


class QuestionsUpdate(BaseModel):
    """Schema for partial question updates."""
    pergunta: Optional[str] = None
    resposta_a: Optional[str] = None
    resposta_b: Optional[str] = None
    resposta_c: Optional[str] = None
    resposta_d: Optional[str] = None
    resposta_certa: Optional[str] = None
    questao_completa: Optional[str] = None
    explicacao_a: Optional[str] = None
    explicacao_b: Optional[str] = None
    explicacao_c: Optional[str] = None
    explicacao_d: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "pergunta": "Qual é a capital do Brasil?",
                "resposta_certa": "C"
            }
        }


class QuestionsPost(QuestionsBase):
    """Schema for creating a new question."""
    pass


class QuestionsGet(QuestionsBase):
    """Schema for retrieving question data with ID."""
    id: UUID

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "pergunta": "Qual é a capital do Brasil?",
                "resposta_a": "São Paulo",
                "resposta_b": "Rio de Janeiro",
                "resposta_c": "Brasília",
                "resposta_d": "Belo Horizonte",
                "resposta_certa": "C",
                "questao_completa": "Pergunta: Qual é a capital do Brasil?\nA) São Paulo\nB) Rio de Janeiro\nC) Brasília\nD) Belo Horizonte",
                "explicacao_a": "São Paulo é a maior cidade, mas não a capital.",
                "explicacao_b": "Rio de Janeiro foi a capital antiga.",
                "explicacao_c": "Brasília é a capital atual.",
                "explicacao_d": "Belo Horizonte é uma cidade importante, mas não a capital."
            }
        }