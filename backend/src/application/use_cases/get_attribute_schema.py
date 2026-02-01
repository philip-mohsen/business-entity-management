# File: backend/src/application/use_cases/get_attribute_schema.py

from src.domain.models.identifier import AttributeIdentifier
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.application.dtos.attribute_schema_dto import AttributeSchemaDTO
from src.application.mappers.attribute_schema_mapper import AttributeSchemaMapper

class GetAttributeSchemaUseCase:
    def __init__(self, repository: IAttributeSchemaRepository):
        self.repository = repository
        self.mapper = AttributeSchemaMapper

    def execute(self, attribute_schema_id_value: str) -> AttributeSchemaDTO:
        attribute_schema_id = AttributeIdentifier(attribute_schema_id_value)
        attribute_schema = self.repository.get(attribute_schema_id)
        
        if attribute_schema is None:
            raise ValueError(f"AttributeSchema with id {attribute_schema_id.value} not found")
        
        return self.mapper.to_dto(attribute_schema)
