# File: src/infrastructure/persistence/repositories/json/attribute_schema_repository.py

from src.domain.models.attributes import AttributeSchema
from src.domain.models.identifier import Identifier
from src.domain.interfaces.repositories.attribute_schema_repository import IAttributeSchemaRepository
from src.infrastructure.connectors.file_connector import FileConnector

class JsonAttributeSchemaRepository(IAttributeSchemaRepository):
    def __init__(self, connector: FileConnector):
        self.connector = connector
        self.collection = "attribute_schemas"

    def save(self, attribute_schema: AttributeSchema) -> None:
        all_data = self.connector.read_json(self.collection)
        all_data[attribute_schema.id.value] = attribute_schema.model_dump()
        self.connector.write_json(self.collection, all_data)

    def get_by_id(self, id: Identifier) -> AttributeSchema:
        pass

    def delete(self, id: Identifier) -> None:
        pass
