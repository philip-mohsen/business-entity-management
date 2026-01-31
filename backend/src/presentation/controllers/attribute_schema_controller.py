# File: backend/src/presentation/controllers/attribute_schema_controller.py

from src.application.use_cases.create_attribute_schema import CreateAttributeSchemaUseCase
from src.application.use_cases.validate_attribute_value import ValidateAttributeValueUseCase
from src.application.dtos.attribute_schema_dto import CreateAttributeSchemaRequest
from src.application.dtos.attribute_schema_dto import AttributeSchemaResponse
from src.application.dtos.attribute_schema_dto import ValidateValueRequest
from src.application.dtos.attribute_schema_dto import ValidationResponse

class AttributeSchemaController:
    def __init__(
            self, 
            create_use_case: CreateAttributeSchemaUseCase,
            validate_use_case: ValidateAttributeValueUseCase
        ):

        self.create_use_case = create_use_case
        self.validate_use_case = validate_use_case
        
    def create(self, dto: CreateAttributeSchemaRequest) -> AttributeSchemaResponse:
        attribute_schema = self.create_use_case.execute(dto)
        response = attribute_schema.model_dump()
        return AttributeSchemaResponse.model_validate(response)
    
    def validate_value(self, dto: ValidateValueRequest) -> ValidationResponse:
        try:
            self.validate_use_case.execute(dto.attribute_schema_id, dto.value)
            return ValidationResponse(is_valid=True)
        except ValueError as ve:
            return ValidationResponse(is_valid=False, message=str(ve), error_type="ValueError")
