from http import HTTPStatus

from ninja import Router

from django_ninja_project.common.api.responses import ErrorResponse
from django_ninja_project.rest_api.facility.api.delete_facility_by_id import delete_facility_by_id
from django_ninja_project.rest_api.facility.api.create_facility import create_facility
from django_ninja_project.rest_api.facility.api.get_facility_by_id import get_facility_by_id
from django_ninja_project.rest_api.facility.api.get_facility_list import get_facility_list
from django_ninja_project.rest_api.facility.api.patch_facility_by_id import patch_facility_by_id
from django_ninja_project.rest_api.facility.api.put_facility_by_id import put_facility_by_id
from django_ninja_project.rest_api.facility.schemas.output import FacilityBaseOutputSchema

facility_router = Router(tags=["Facility"])

facility_router.add_api_operation(
    methods=['GET'],
    path='/',
    response={
        HTTPStatus.OK: list[FacilityBaseOutputSchema]
    },
    view_func=get_facility_list,
    summary="Get Facility list",
)

facility_router.add_api_operation(
    methods=['GET'],
    path='/{facility_id}',
    response={
        HTTPStatus.OK: FacilityBaseOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=get_facility_by_id,
    summary="Get Facility by id",
)

facility_router.add_api_operation(
    methods=['POST'],
    path='/',
    response={
        HTTPStatus.CREATED: FacilityBaseOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse,
    },
    view_func=create_facility,
    summary="Create Facility",
    auth=None
)

facility_router.add_api_operation(
    methods=['PATCH'],
    path='/{facility_id}',
    response={
        HTTPStatus.OK: FacilityBaseOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=patch_facility_by_id,
    summary="Partial update Facility by id",
)

facility_router.add_api_operation(
    methods=['PUT'],
    path='/{facility_id}',
    response={
        HTTPStatus.OK: FacilityBaseOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=put_facility_by_id,
    summary="Full update Facility by id",
)

facility_router.add_api_operation(
    methods=['DELETE'],
    path='/{facility_id}',
    response={
        HTTPStatus.OK: FacilityBaseOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=delete_facility_by_id,
    summary="Delete Facility by id",
)
