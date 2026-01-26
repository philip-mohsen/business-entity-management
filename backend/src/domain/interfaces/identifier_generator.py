# File: backend/src/domain/interfaces/identifier_generator.py

from abc import ABC, abstractmethod
from src.domain.models.identifier import IdPrefix
from src.domain.models.identifier import Identifier

class IIdentifierGenerator(ABC):
    @abstractmethod
    def generate(self, prefix: IdPrefix) -> Identifier:
        pass
