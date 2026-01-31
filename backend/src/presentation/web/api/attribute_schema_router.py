# File: backend/src/presentation/web/api/attribute_schema_router.py

from fastapi import APIRouter, Depends, status
from src.container import container
from src.application.dtos.attribute_schema_dto import CreateAttributeSchemaRequest, AttributeSchemaResponse
from src.application.dtos.attribute_schema_dto import ValidateValueRequest, ValidationResponse
from src.presentation.controllers.attribute_schema_controller import AttributeSchemaController

router = APIRouter(
    prefix="/attribute-schemas",
    tags=["Attribute Schemas"]
)

# Helper function for FastAPI dependency injection
def get_attribute_controller():
    return container.attribute_schema_controller

@router.post("/", response_model=AttributeSchemaResponse, status_code=status.HTTP_201_CREATED)
def create_attribute_schema(
    request: CreateAttributeSchemaRequest,
    controller: AttributeSchemaController = Depends(get_attribute_controller)
):
    return controller.create(request)

@router.post("/validate", response_model=ValidationResponse, status_code=status.HTTP_200_OK)
def validate_attribute_value(
    request: ValidateValueRequest,
    controller: AttributeSchemaController = Depends(get_attribute_controller)
):
    return controller.validate_value(request)
