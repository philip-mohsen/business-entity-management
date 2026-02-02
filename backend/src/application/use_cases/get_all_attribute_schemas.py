# File: backend/src/application/use_cases/get_all_attribute_schemas.py

from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.application.dtos.attribute_schema_dto import AttributeSchemaDTO
from src.application.mappers.attribute_schema_mapper import AttributeSchemaMapper

class GetAllAttributeSchemasUseCase:
    def __init__(self, repository: IAttributeSchemaRepository):
        self.repository = repository
        self.mapper = AttributeSchemaMapper()

    def execute(self) -> list[AttributeSchemaDTO]:
        attribute_schemas = self.repository.get_all()
        return [self.mapper.to_dto(attr) for attr in attribute_schemas]
