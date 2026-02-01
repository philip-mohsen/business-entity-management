# File: backend/src/domain/interfaces/repositories/attribute_schema_repository.py

from abc import ABC, abstractmethod
from typing import Optional
from src.domain.models.attributes import AttributeSchema
from src.domain.models.identifier import AttributeIdentifier

class IAttributeSchemaRepository(ABC):
    @abstractmethod
    def get(self, id: AttributeIdentifier) -> Optional[AttributeSchema]:
        """
        Retrieve an attribute by its unique identifier.
        Returns None if no attribute is found.
        """
        pass

    @abstractmethod
    def save(self, attribute_schema: AttributeSchema) -> None:
        """
        Persist the attribute schema.
        """
        pass

    @abstractmethod
    def delete(self, id: AttributeIdentifier) -> None:
        """
        Remove an attribute schema from the persistence layer.
        """
        pass
