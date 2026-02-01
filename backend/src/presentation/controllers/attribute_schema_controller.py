# File: backend/src/presentation/controllers/attribute_schema_controller.py

from src.application.use_cases.get_attribute_schema import GetAttributeSchemaUseCase
from src.application.use_cases.create_attribute_schema import CreateAttributeSchemaUseCase
from src.application.use_cases.validate_attribute_value import ValidateAttributeValueUseCase
from src.application.dtos.attribute_schema_dto import AttributeSchemaRequest, AttributeSchemaDTO
from src.application.dtos.attribute_validation_dto import ValueValidationRequest, ValueValidationResponse

class AttributeSchemaController:
    def __init__(
            self, 
            create_use_case: CreateAttributeSchemaUseCase,
            get_use_case: GetAttributeSchemaUseCase,
            validate_use_case: ValidateAttributeValueUseCase
        ):

        self.create_use_case = create_use_case
        self.get_use_case = get_use_case
        self.validate_use_case = validate_use_case

    def create(self, dto: AttributeSchemaRequest) -> AttributeSchemaDTO:
        attribute_schema = self.create_use_case.execute(dto)
        return attribute_schema

    def get(self, id_value: str) -> AttributeSchemaDTO:
        return self.get_use_case.execute(id_value)
    
    def validate(self, id_value: str, request: ValueValidationRequest) -> ValueValidationResponse:
        return self.validate_use_case.execute(id_value, request)
