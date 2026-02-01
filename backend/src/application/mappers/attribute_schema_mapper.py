# File: backend/src/application/mappers/attribute_schema_mapper.py

from src.domain.models.attributes import AttributeSchema
from src.application.dtos.attribute_schema_dto import AttributeSchemaDTO, AttributeSchemaRequest

class AttributeSchemaMapper:
    @staticmethod
    def to_domain(request: AttributeSchemaRequest, new_id: str) -> AttributeSchema:
        data = request.model_dump(mode="json", exclude_none=True)
        data["id"] = new_id
        attribute_schema = AttributeSchema.model_validate(data)
        return attribute_schema

    @staticmethod
    def to_dto(domain: AttributeSchema) -> AttributeSchemaDTO:
        data = domain.model_dump(mode="json", exclude_none=True)
        return AttributeSchemaDTO.model_validate(data, from_attributes=True)
