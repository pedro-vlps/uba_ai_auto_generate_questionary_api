from enum import Enum
from pydantic import BaseModel


class ParameterEnum(str, Enum):
    """Enumeration of allowed anatomy topics for question generation."""
    NEURO = "Neuro"
    ESPLACNO = "Esplacno"
    LOCOMOTOR = "Locomotor"


class AnatomySchema(BaseModel):
    """Schema for anatomy question generation request."""
    parameter: ParameterEnum

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "parameter": "Neuro"
            }
        }
