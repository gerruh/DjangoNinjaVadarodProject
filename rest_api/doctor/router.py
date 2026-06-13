from http import HTTPStatus

from ninja import Router

from common.api.responses import ErrorResponse
from rest_api.doctor.api.create_doctor import create_doctor
from rest_api.doctor.api.delete_doctor_by_id import delete_doctor_by_id
from rest_api.doctor.api.get_doctor_by_id import get_doctor_by_id
from rest_api.doctor.api.get_doctor_list import get_doctor_list
from rest_api.doctor.api.patch_doctor_by_id import patch_doctor_by_id
from rest_api.doctor.schemas.output import DoctorBaseOutputSchema, DoctorDetailOutputSchema, \
    DoctorListOutputSchema

doctor_router = Router(tags=["Doctor"])

doctor_router.add_api_operation(
    methods=["GET"],
    path="/",
    response={
        HTTPStatus.OK: list[DoctorListOutputSchema],
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=get_doctor_list,
    summary="Get Doctor list",
)

doctor_router.add_api_operation(
    methods=["GET"],
    path="/{doctor_id}",
    response={
        HTTPStatus.OK: DoctorDetailOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=get_doctor_by_id,
    summary="Get Doctor by id",
)

doctor_router.add_api_operation(
    methods=["POST"],
    path="/",
    response={
        HTTPStatus.CREATED: DoctorBaseOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=create_doctor,
    summary="Create Doctor",
)

doctor_router.add_api_operation(
    methods=["PATCH"],
    path="/{doctor_id}",
    response={
        HTTPStatus.OK: DoctorDetailOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
        HTTPStatus.CONFLICT: ErrorResponse,
    },
    view_func=patch_doctor_by_id,
    summary="Partially update Doctor",
)

doctor_router.add_api_operation(
    methods=["DELETE"],
    path="/{doctor_id}",
    response={
        HTTPStatus.OK: DoctorDetailOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
    },
    view_func=delete_doctor_by_id,
    summary="Delete Doctor",
)
