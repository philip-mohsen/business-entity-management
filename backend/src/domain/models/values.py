# File: backend/src/domain/models/values.py

from enum import StrEnum
from typing import Annotated, Literal, Union
from pydantic import BaseModel, ConfigDict, Field, model_validator

class ValueType(StrEnum):
    TEXT = "text"
    INTEGER = "integer"
    DATE = "date"
    BOOLEAN = "boolean"

class AttributeValueSchemaBase(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid"
    )
    type: ValueType

class TextValueSchema(AttributeValueSchemaBase):
    type: Literal[ValueType.TEXT] = Field(default=ValueType.TEXT)
    min_length: int | None = Field(default=None, ge=0)
    max_length: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def validate_length_constraints(self) -> "TextValueSchema":
        if self.min_length is not None and self.max_length is not None:
            if self.min_length > self.max_length:
                raise ValueError("min_length cannot be greater than max_length")
        return self

class IntegerValueSchema(AttributeValueSchemaBase):
    type: Literal[ValueType.INTEGER] = Field(default=ValueType.INTEGER)
    min_value: int | None = Field(default=None)
    max_value: int | None = Field(default=None)

    @model_validator(mode="after")
    def validate_value_constraints(self) -> "IntegerValueSchema":
        if self.min_value is not None and self.max_value is not None:
            if self.min_value > self.max_value:
                raise ValueError("min_value cannot be greater than max_value")
        return self

AttributeValueSchema = Annotated[
    Union[TextValueSchema, IntegerValueSchema],
    Field(discriminator="type")
]
