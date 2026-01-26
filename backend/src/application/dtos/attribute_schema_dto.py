# File: backend/src/application/dtos/attribute_schema_dto.py

from pydantic import BaseModel, Field

class CreateAttributeSchemaRequest(BaseModel):
    name: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)
    max_length: int | None = Field(default=255, ge=1)

class AttributeSchemaResponse(BaseModel):
    id: str
    name: str
    label: str
    type: str
    max_length: int
