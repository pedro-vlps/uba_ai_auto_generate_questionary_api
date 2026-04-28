"""Pydantic schemas for question data validation and serialization."""
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class QuestionsBase(BaseModel):
    """Base schema for multiple-choice question data."""
    question: str
    answer_a: str
    answer_b: str
    answer_c: str
    answer_d: str
    correct_answer: str
    explanation_a: Optional[str] = None
    explanation_b: Optional[str] = None
    explanation_c: Optional[str] = None
    explanation_d: Optional[str] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "question": "Qual é a capital do Brasil?",
                "answer_a": "São Paulo",
                "answer_b": "Rio de Janeiro",
                "answer_c": "Brasília",
                "answer_d": "Belo Horizonte",
                "correct_answer": "C",
                "explanation_a": "São Paulo é a maior cidade, mas não a capital.",
                "explanation_b": "Rio de Janeiro foi a capital antiga.",
                "explanation_c": "Brasília é a capital atual.",
                "explanation_d": "Belo Horizonte é uma cidade importante, mas não a capital."
            }
        }


class QuestionsGet(QuestionsBase):
    """Schema for retrieving question data with ID."""
    id: UUID
    institution_id: UUID
    topic: str
    subject: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "question": "Qual é a capital do Brasil?",
                "answer_a": "São Paulo",
                "answer_b": "Rio de Janeiro",
                "answer_c": "Brasília",
                "answer_d": "Belo Horizonte",
                "correct_answer": "C",
                "explanation_a": "São Paulo é a maior cidade, mas não a capital.",
                "explanation_b": "Rio de Janeiro foi a capital antiga.",
                "explanation_c": "Brasília é a capital atual.",
                "explanation_d": "Belo Horizonte é uma cidade importante, mas não a capital."
            }
        }

class OnlyQuestionsGetSchema(BaseModel):
    """Schema for retrieving question data without ID."""
    question: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "question": "Qual é a capital do Brasil?"
            }
        }
