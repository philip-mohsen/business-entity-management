# File: backend/src/domain/interfaces/services/value_validator_service.py

from abc import ABC, abstractmethod
from typing import Any
from src.domain.models.attributes import AttributeSchema

class IValueValidatorService(ABC):
    @abstractmethod
    def validate(self, attribute_schema: AttributeSchema, value: Any) -> None:
        pass
