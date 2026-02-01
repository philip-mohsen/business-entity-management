# File: backend/src/domain/models/attributes.py

from pydantic import BaseModel, ConfigDict
from src.domain.models.identifier import AttributeIdentifier
from src.domain.models.values import AttributeValueSchema

class AttributeSchema(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    id: AttributeIdentifier
    name: str
    label: str
    value_schema: AttributeValueSchema
