# File: src/infrastructure/persistence/repositories/json/attribute_schema_repository.py

from typing import Optional
from src.domain.models.attributes import AttributeSchema
from src.domain.models.identifier import AttributeIdentifier
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.infrastructure.connectors.file_connector import FileConnector

class JsonAttributeSchemaRepository(IAttributeSchemaRepository):
    def __init__(self, connector: FileConnector):
        self.connector = connector
        self.collection = "attribute_schemas"

    def save(self, attribute_schema: AttributeSchema) -> None:
        data = self.connector.read_json(self.collection)
        data[attribute_schema.id.value] = attribute_schema.model_dump(mode="json", exclude_none=True)
        self.connector.write_json(self.collection, data)
        
    def get(self, id: AttributeIdentifier) -> Optional[AttributeSchema]:
        pass

    def delete(self, id: AttributeIdentifier) -> None:
        pass
