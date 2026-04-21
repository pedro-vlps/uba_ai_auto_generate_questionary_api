from enum import Enum
from pydantic import BaseModel


class ParameterEnum(str, Enum):
    NEURO = "Neuro"
    ESPLACNO = "Esplacno"
    LOCOMOTOR = "Locomotor"


class AnatomySchema(BaseModel):
    parameter: ParameterEnum

    class Config:
        """Configure Pydantic to allow population from ORM objects and provide an example."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "parameter": "Neuro"
            }
        }
