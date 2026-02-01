# File: backend/src/domain/models/identifier.py

from enum import StrEnum
from pydantic import RootModel, ConfigDict, field_validator

class IdPrefix(StrEnum):
    ATTR = "ATTR"

class Identifier(RootModel[str]):
    model_config = ConfigDict(
        frozen=True
    )

    @field_validator("root", mode="after")
    @classmethod
    def validate_not_empty_identifier(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Identifier cannot be empty")
        return v
    
    @property
    def value(self) -> str:
        return self.root

    def __str__(self) -> str:
        return self.root

class AttributeIdentifier(Identifier):
    @field_validator("root", mode="after")
    @classmethod
    def validate_prefix(cls, v: str) -> str:
        prefix = f"{IdPrefix.ATTR}-"
        if not v.startswith(prefix):
            raise ValueError(f"AttributeIdentifier must start with prefix '{prefix}'")
        return v
