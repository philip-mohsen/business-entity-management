# File: backend/src/domain/models/values.py

from enum import StrEnum
from typing import Annotated, Literal, Union
from pydantic import BaseModel, ConfigDict, Field

class ValueType(StrEnum):
    TEXT = "string"
    INTEGER = "number"
    DATE = "date"
    BOOLEAN = "boolean"

class AttributeValueSchemaBase(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

class TextValueSchema(AttributeValueSchemaBase):    
    type: Literal[ValueType.TEXT] = Field(default=ValueType.TEXT, serialization_alias="type")
    min_length: int | None = Field(default=0, ge=0, serialization_alias="minLength")
    max_length: int | None = Field(default=255, ge=1, serialization_alias="maxLength")

class IntegerValueSchema(AttributeValueSchemaBase):
    type: Literal[ValueType.INTEGER] = Field(default=ValueType.INTEGER, serialization_alias="type")
    min_value: int | None = Field(default=None, serialization_alias="minimum")
    max_value: int | None = Field(default=None, serialization_alias="maximum")

AttributeValueSchemaT = Annotated[
    Union[TextValueSchema, IntegerValueSchema], 
    Field(discriminator="type")
]
