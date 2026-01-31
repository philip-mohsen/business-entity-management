# File: backend/src/domain/models/attributes.py

from pydantic import BaseModel
from src.domain.models.identifier import Identifier
from src.domain.models.values import AttributeValueSchemaT

class AttributeSchema(BaseModel):
    id: Identifier
    name: str
    label: str
    value_schema: AttributeValueSchemaT
