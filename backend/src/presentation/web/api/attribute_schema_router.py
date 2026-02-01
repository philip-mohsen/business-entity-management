# File: backend/src/presentation/web/api/attribute_schema_router.py

from fastapi import APIRouter, Depends, status
from src.container import container
from src.application.dtos.attribute_schema_dto import AttributeSchemaRequest, AttributeSchemaDTO
from src.application.dtos.attribute_validation_dto import ValueValidationRequest, ValueValidationResponse
from src.presentation.controllers.attribute_schema_controller import AttributeSchemaController

router = APIRouter(
    prefix="/attribute-schemas",
    tags=["Attribute Schemas"]
)

# Helper function for FastAPI dependency injection
def get_attribute_controller():
    return container.attribute_schema_controller

@router.post(
        "/", 
        response_model=AttributeSchemaDTO, 
        response_model_by_alias=True,
        response_model_exclude_none=True,
        status_code=status.HTTP_201_CREATED
)
def create_attribute_schema(
    request: AttributeSchemaRequest,
    controller: AttributeSchemaController = Depends(get_attribute_controller)
):  
    return controller.create(request)

@router.get(
        "/{attribute_schema_id}", 
        response_model=AttributeSchemaDTO, 
        response_model_by_alias=True,
        response_model_exclude_none=True,
        status_code=status.HTTP_200_OK
)
def get_attribute_schema(
    attribute_schema_id: str,
    controller: AttributeSchemaController = Depends(get_attribute_controller)
):
    return controller.get(attribute_schema_id)

@router.get(
        "/{attribute_schema_id}/validate", 
        response_model=ValueValidationResponse, 
        response_model_by_alias=True
)
def validate_attribute_value(
    attribute_schema_id: str,
    request: ValueValidationRequest,
    controller: AttributeSchemaController = Depends(get_attribute_controller)
):
    return controller.validate(attribute_schema_id, request)
