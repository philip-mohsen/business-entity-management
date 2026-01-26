# File: backend/src/domain/models/attributes.py

from typing import Literal
from pydantic import BaseModel
from src.domain.models.identifier import Identifier

class AttributeSchema(BaseModel):
    id: Identifier
    name: str
    label: str
    type: str

class TextAttributeSchema(AttributeSchema):
    max_length: int | None = 255
    type: Literal["text"] = "text"
    
class NumberAttributeSchema(AttributeSchema):
    type: Literal["number"] = "number"
