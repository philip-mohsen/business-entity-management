# File: backend/src/application/dtos/attribute_schema_dto.py

from typing import Any
from pydantic import BaseModel, Field
from src.domain.models.values import AttributeValueSchemaT

class CreateAttributeSchemaRequest(BaseModel):
    name: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    value_schema: AttributeValueSchemaT

class AttributeSchemaResponse(BaseModel):
    id: str
    name: str
    label: str
    value_schema: AttributeValueSchemaT

class ValidateValueRequest(BaseModel):
    attribute_schema_id: str
    value: Any
    
class ValidationResponse(BaseModel):
    is_valid: bool
    message: str | None = None
    error_type: str | None = None
