# File: backend/src/application/use_cases/validate_attribute_value.py

from typing import Any
from src.domain.models.identifier import AttributeIdentifier
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.domain.interfaces.services.value_validator_service import IValueValidatorService
from src.application.dtos.attribute_validation_dto import ValueValidationRequest, ValueValidationResponse

class ValidateAttributeValueUseCase:
    def __init__(
        self,
        repository: IAttributeSchemaRepository,
        validator_service: IValueValidatorService
    ):
        self.repository = repository
        self.validator_service = validator_service

    def execute(self, attribute_schema_id_value: str, request: ValueValidationRequest) -> ValueValidationResponse:
        attribute_schema_id = AttributeIdentifier(attribute_schema_id_value)
        attribute_schema = self.repository.get(attribute_schema_id)

        if attribute_schema is None:
            return ValueValidationResponse(
                value=request.value,
                is_valid=False,
                message=f"AttributeSchema with id {attribute_schema_id_value} not found"
            )

        try:
            self.validator_service.validate(attribute_schema, request.value)
            return ValueValidationResponse(
                value=request.value,
                is_valid=True,
                message=None
            )
        
        except ValueError as e:
            return ValueValidationResponse(
                value=request.value,
                is_valid=False,
                message=str(e)
            )
