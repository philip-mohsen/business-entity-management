# File: backend/src/domain/factories/attribute_schema_factory.py

from typing import Dict, Any
from typing import Union, Annotated
from pydantic import Field, RootModel

from src.domain.models.attributes import TextAttributeSchema
from src.domain.models.attributes import NumberAttributeSchema

AttributeSchemaUnion = Annotated[
    Union[TextAttributeSchema, NumberAttributeSchema],
    Field(discriminator="type")
]

class AttributeSchemaFactory:
    @classmethod
    def create(cls, data: Dict[str, Any]) -> AttributeSchemaUnion:
        return RootModel[AttributeSchemaUnion].model_validate(data).root
