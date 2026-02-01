# File: backend/src/application/dtos/attribute_validation_dto.py

from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class ValueValidationRequest(BaseModel):
    value: Any = Field(..., description="The value to validate against the schema")

class ValueValidationResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    value: Any = Field(..., description="The value that was validated")
    is_valid: bool = Field(..., alias="isValid")
    message: str | None = Field(None, description="Error message if validation fails")
