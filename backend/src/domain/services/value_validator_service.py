from typing import Any
from jsonschema import validate, ValidationError as JsonSchemaError
from src.domain.models.attributes import AttributeSchema

class ValueValidatorService:
    @staticmethod
    def validate(attribute: AttributeSchema, value: Any) -> bool:
        schema = attribute.value_schema.model_dump(
            mode="json",
            by_alias=True,
            exclude_none=True
        )

        print(schema)

        try:
            validate(instance=value, schema=schema)
            return True
        
        except JsonSchemaError as e:
            raise ValueError(f"Invalid value for attribute '{attribute.name}': {e.message}") from e
