# File: backend/src/presentation/controllers/attribute_schema_controller.py

from src.application.use_cases.create_attribute_schema import CreateAttributeSchemaUseCase
from src.application.dtos.attribute_schema_dto import AttributeSchemaRequest, AttributeSchemaDTO

class AttributeSchemaController:
    def __init__(
            self, 
            create_use_case: CreateAttributeSchemaUseCase
        ):

        self.create_use_case = create_use_case
        
    def create(self, dto: AttributeSchemaRequest) -> AttributeSchemaDTO:
        attribute_schema = self.create_use_case.execute(dto)
        return attribute_schema
