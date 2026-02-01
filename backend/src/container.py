# File: backend/src/container.py

from src.presentation.controllers.attribute_schema_controller import AttributeSchemaController
from src.application.use_cases.create_attribute_schema import CreateAttributeSchemaUseCase
from src.application.use_cases.get_attribute_schema import GetAttributeSchemaUseCase
from src.application.use_cases.validate_attribute_value import ValidateAttributeValueUseCase
from src.infrastructure.connectors.file_connector import FileConnector
from src.infrastructure.identifiers.attribute_schema_identifier_generator import AttributeSchemaIdentifierGenerator
from src.infrastructure.persistence.repositories.attribute_schema_repository import JsonAttributeSchemaRepository
from src.infrastructure.validators.jsonschema_validator_service import JsonSchemaValidatorService

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

        self.get_use_case = GetAttributeSchemaUseCase(
            repository=self.attribute_schema_repository
        )

        self.validate_attribute_value_use_case = ValidateAttributeValueUseCase(
            repository=self.attribute_schema_repository,
            validator_service=JsonSchemaValidatorService()
        )
        
        # 5. Controllers
        self.attribute_schema_controller = AttributeSchemaController(
            create_use_case=self.create_attribute_schema_use_case,
            get_use_case=self.get_use_case,
            validate_use_case=self.validate_attribute_value_use_case
        )

# Create a singleton instance to be used by Presentation layer
container = Container()
