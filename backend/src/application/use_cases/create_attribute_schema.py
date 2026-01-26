# File: src/application/use_cases/create_attribute_schema.py

from src.domain.models.attributes import AttributeSchema
from src.domain.models.identifier import IdPrefix
from src.domain.factories.attribute_schema_factory import AttributeSchemaFactory
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.domain.interfaces.identifier_generator import IIdentifierGenerator
from src.application.dtos.attribute_schema_dto import CreateAttributeSchemaRequest 

class CreateAttributeSchemaUseCase:
    def __init__(
            self,
            repository: IAttributeSchemaRepository,
            factory: AttributeSchemaFactory,
            identifier_generator: IIdentifierGenerator
        ):
        self.repository = repository
        self.factory = factory
        self.identifier_generator = identifier_generator

    def execute(self, data: CreateAttributeSchemaRequest) -> AttributeSchema:
        data_dict = data.model_dump()
        data_dict["id"] = self.identifier_generator.generate(IdPrefix.ATTR)
        attribute_schema = self.factory.create(data_dict)
        self.repository.save(attribute_schema)
        return attribute_schema
