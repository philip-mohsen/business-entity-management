# File: backend/src/domain/models/identifier.py

from enum import Enum
from pydantic import RootModel

class IdPrefix(str, Enum):
    ATTR = "ATTR"

class Identifier(RootModel[str]):
    @property
    def value(self) -> str:
        return self.root

    def __str__(self) -> str:
        return self.root
