# File: backend/src/infrastructure/identifiers/prefixed_identifier_generator.py

import uuid
from src.domain.interfaces.identifier_generator import IIdentifierGenerator
from src.domain.models.identifier import IdPrefix
from src.domain.models.identifier import Identifier

class PrefixedIdentifierGenerator(IIdentifierGenerator):
    def generate(self, prefix: IdPrefix) -> Identifier:
        short = str(uuid.uuid4()).split("-")[0].upper()
        return Identifier(f"{prefix.value}-{short}")
