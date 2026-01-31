# File: backend/src/domain/factories/attribute_schema_factory.py

from typing import Dict, Any
from pydantic import RootModel

from src.domain.models.attributes import AttributeSchema

class AttributeSchemaFactory:
    @classmethod
    def create(cls, data: Dict[str, Any]) -> AttributeSchema:
        return AttributeSchema.model_validate(data)
