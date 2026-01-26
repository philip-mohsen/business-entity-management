# File: backend/src/domain/interfaces/repositories/attribute_schema_repository.py

from abc import ABC, abstractmethod
from src.domain.models.attributes import AttributeSchema
from src.domain.models.identifier import Identifier

class IAttributeSchemaRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: Identifier) -> AttributeSchema:
        pass

    @abstractmethod
    def save(self, attribute_schema: AttributeSchema) -> None:
        pass

    @abstractmethod
    def delete(self, id: Identifier) -> None:
        pass
