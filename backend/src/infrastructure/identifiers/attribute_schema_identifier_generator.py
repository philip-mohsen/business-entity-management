# File: backend/src/infrastructure/identifiers/attribute_schema_identifier_generator.py

import uuid
from src.domain.interfaces.identifier_generator import IIdentifierGenerator
from src.domain.models.identifier import IdPrefix
from src.domain.models.identifier import AttributeIdentifier

class AttributeSchemaIdentifierGenerator(IIdentifierGenerator):
    def generate(self, prefix: IdPrefix) -> AttributeIdentifier:
        short = str(uuid.uuid4()).split("-")[0].upper()
        return AttributeIdentifier(f"{prefix.value}-{short}")
