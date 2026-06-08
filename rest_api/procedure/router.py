from http import HTTPStatus

from ninja import Router

from common.api.responses import ErrorResponse
from rest_api.procedure.api.create_procedure import create_procedure
from rest_api.procedure.api.delete_procedure_by_id import delete_procedure_by_id
from rest_api.procedure.api.get_procedure_by_id import get_procedure_by_id
from rest_api.procedure.api.get_procedure_list import get_procedure_list
from rest_api.procedure.api.patch_procedure_by_id import patch_procedure_by_id
from rest_api.procedure.api.put_procedure_by_id import put_procedure_by_id
from rest_api.procedure.schemas.output import ProcedureOutputSchema

procedure_router = Router(tags=["Procedure"])

procedure_router.add_api_operation(
    methods=['GET'],
    path='/',
    response={
        HTTPStatus.OK: list[ProcedureOutputSchema],
        HTTPStatus.NOT_FOUND: ErrorResponse
    },
    view_func=get_procedure_list,
    summary="Get Procedure list"
)

procedure_router.add_api_operation(
    methods=['GET'],
    path='/{procedure_id}',
    response={
        HTTPStatus.OK: ProcedureOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse
    },
    view_func=get_procedure_by_id,
    summary="Get Procedure by id",
)

procedure_router.add_api_operation(
    methods=['POST'],
    path='/',
    response={
        HTTPStatus.OK: ProcedureOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse
    },
    view_func=create_procedure,
    summary="Create Procedure",
)

procedure_router.add_api_operation(
    methods=['PATCH'],
    path='/{procedure_id}',
    response={
        HTTPStatus.OK: ProcedureOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
        HTTPStatus.CONFLICT: ErrorResponse
    },
    view_func=patch_procedure_by_id,
    summary="Partially update Procedure",
)

procedure_router.add_api_operation(
    methods=['PUT'],
    path='/{procedure_id}',
    response={
        HTTPStatus.OK: ProcedureOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse,
        HTTPStatus.CONFLICT: ErrorResponse
    },
    view_func=put_procedure_by_id,
    summary="Fully update Procedure",
)

procedure_router.add_api_operation(
    methods=['DELETE'],
    path='/{procedure_id}',
    response={
        HTTPStatus.OK: ProcedureOutputSchema,
        HTTPStatus.NOT_FOUND: ErrorResponse
    },
    view_func=delete_procedure_by_id,
    summary="Delete Procedure",
)

