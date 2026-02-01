# File: backend/src/container.py

from src.presentation.controllers.attribute_schema_controller import AttributeSchemaController
from src.application.use_cases.create_attribute_schema import CreateAttributeSchemaUseCase
from src.infrastructure.connectors.file_connector import FileConnector
from src.infrastructure.identifiers.attribute_schema_identifier_generator import AttributeSchemaIdentifierGenerator
from src.infrastructure.persistence.repositories.json.attribute_schema_repository import JsonAttributeSchemaRepository

class Container:
    """Manages the dependencies for the application."""

    def __init__(self):
        # 1. Infracstructure Layer (Low-Level)
        self.connector = FileConnector(base_path="D:\\projects\\business-entity-management\\data")
        self.id_generator = AttributeSchemaIdentifierGenerator()

        # 2. Persistence Repositories
        self.attribute_schema_repository = JsonAttributeSchemaRepository(connector=self.connector)

        # 4. Application Use Cases
        self.create_attribute_schema_use_case = CreateAttributeSchemaUseCase(
            repository=self.attribute_schema_repository,
            identifier_generator=self.id_generator
        )

        # 5. Controllers
        self.attribute_schema_controller = AttributeSchemaController(
            create_use_case=self.create_attribute_schema_use_case
        )

# Create a singleton instance to be used by Presentation layer
container = Container()
