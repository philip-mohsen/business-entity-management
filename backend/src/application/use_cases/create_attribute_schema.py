# File: src/application/use_cases/create_attribute_schema.py

from src.domain.models.attributes import AttributeSchema
from src.domain.models.identifier import IdPrefix
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.domain.interfaces.identifier_generator import IIdentifierGenerator
from src.application.dtos.attribute_schema_dto import AttributeSchemaRequest, AttributeSchemaDTO
from src.application.mappers.attribute_schema_mapper import AttributeSchemaMapper

class CreateAttributeSchemaUseCase:
    def __init__(
            self,
            repository: IAttributeSchemaRepository,
            identifier_generator: IIdentifierGenerator
        ):
        self.repository = repository
        self.identifier_generator = identifier_generator
        self.mapper = AttributeSchemaMapper

    def execute(self, data: AttributeSchemaRequest) -> AttributeSchemaDTO:
        new_id = self.identifier_generator.generate(IdPrefix.ATTR)
        
        attribute_schema = self.mapper.to_domain(data, new_id)

        self.repository.save(attribute_schema)

        return self.mapper.to_dto(attribute_schema)
