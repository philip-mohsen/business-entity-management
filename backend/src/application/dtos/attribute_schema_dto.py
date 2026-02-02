# File: backend/src/application/dtos/attribute_schema_dto.py

from typing import Annotated, Union, Literal, Set
from pydantic import BaseModel, ConfigDict, Field

class TextValueSchemaDTO(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Literal["text"] = Field(default="text", alias="type", description="Type of the value schema")
    min_length: int | None = Field(
        default=None,
        ge=0,
        alias="minLength",
        description="Minimum length of the text value"
    )
    
    max_length: int | None = Field(
        default=None,
        ge=0,
        alias="maxLength",
        description="Maximum length of the text value"
    )

    pattern: str | None = Field(
        default=None,
        alias="pattern",
        min_length=1,
        description="Regex pattern that the text value must match"
    )

class IntegerValueSchemaDTO(BaseModel):
    model_config = ConfigDict(populate_by_name=True)    
    type: Literal["integer"] = Field(default="integer", alias="type", description="Type of the value schema")

    min_value: int | None = Field(
        default=None,
        ge=0,
        alias="minimum",
        description="Minimum integer value"
    )

    max_value: int | None = Field(
        default=None,
        ge=0,
        alias="maximum",
        description="Maximum integer value"
    )


class ListTextValueSchemaDTO(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: Literal["listtext"] = Field(default="listtext", alias="type", description="Type of the value schema")
    items: Set[str] = Field(
        ...,
        description="List of allowed text values"
    )

AttributeSchemaValueDTO = Annotated[
    Union[TextValueSchemaDTO, IntegerValueSchemaDTO, ListTextValueSchemaDTO], 
    Field(discriminator="type")
]

class AttributeSchemaRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(..., description="System name of the attribute")
    label: str = Field(..., description="Human-readable label for the attribute")
    value_schema: AttributeSchemaValueDTO = Field(
        ..., alias="valueSchema", description="Schema defining the attribute's value"
    )

class AttributeSchemaDTO(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(..., description="Unique identifier of the attribute schema")
    name: str = Field(..., description="System name of the attribute")
    label: str = Field(..., description="Human-readable label for the attribute")
    value_schema: AttributeSchemaValueDTO = Field(
        ..., alias="valueSchema", description="Schema defining the attribute's value"
    )
