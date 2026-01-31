# File: backend/src/application/use_cases/validate_attribute_value.py

from typing import Any
from src.domain.models.identifier import Identifier
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.domain.services.value_validator_service import ValueValidatorService

class ValidateAttributeValueUseCase:
    def __init__(
            self, 
            repository: IAttributeSchemaRepository,
            validator: ValueValidatorService = ValueValidatorService()
        ):
        self.repository = repository
        self.validator = validator

    def execute(self, attribute_schema_id: str, value: Any) -> bool:
        identifier = Identifier(root=attribute_schema_id)
        attribute_schema = self.repository.get_by_id(identifier)
        if not attribute_schema:
            raise ValueError(f"Attribute schema with ID '{attribute_schema_id}' not found.")

        return self.validator.validate(attribute_schema, value)
