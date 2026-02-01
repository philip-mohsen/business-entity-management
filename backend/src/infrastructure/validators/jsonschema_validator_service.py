# File: /backend/src/infrastructure/validators/jsonschema_validator_service.py

from typing import Any, Literal, Type
from jsonschema import validate, ValidationError
from pydantic import BaseModel, ConfigDict, Field
from src.domain.models.attributes import AttributeSchema
from src.domain.models.values import ValueType
from src.domain.interfaces.services.value_validator_service import IValueValidatorService

class JSONSchemaString(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    type: Literal["string"] = Field(default="string", alias="type")
    min_length: int | None = Field(default=None, ge=0, alias="minLength")
    max_length: int | None = Field(default=None, ge=0, alias="maxLength")
    pattern: str | None = Field(default=None, alias="pattern")

class JSONSchemaInteger(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    type: Literal["integer"] = Field(default="integer", alias="type")
    min_value: int | None = Field(default=None, alias="minimum")
    max_value: int | None = Field(default=None, alias="maximum")

class JsonSchemaValidatorService(IValueValidatorService):
    _ADAPTER_MAP: dict[ValueType, Type[BaseModel]] = {
        ValueType.TEXT: JSONSchemaString,
        ValueType.INTEGER: JSONSchemaInteger,
    }

    def validate(self, attribute_schema: AttributeSchema, value: Any) -> None:
        value_schema = attribute_schema.value_schema
        AdapterClass = self._ADAPTER_MAP.get(value_schema.type)

        if not AdapterClass:
            raise NotImplementedError(f"Validation not implemented for {value_schema.type}")
        
        value_schema_data = value_schema.model_dump(mode="json", exclude_none=True, exclude={"type"})
        json_schema = AdapterClass.model_validate(value_schema_data)
        json_schema_data = json_schema.model_dump(mode="json", by_alias=True, exclude_none=True)

        try:
            validate(instance=value, schema=json_schema_data)
        except ValidationError as e:
            raise ValueError(e.message)
