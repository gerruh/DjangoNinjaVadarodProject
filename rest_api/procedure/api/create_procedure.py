from http import HTTPStatus

from django.http import HttpRequest

from rest_api.procedure.schemas.input import ProcedureInputSchema
from rest_api.procedure.schemas.output import ProcedureBaseOutputSchema
from rest_api.procedure.services.create_procedure_service import CreateProcedureService


def create_procedure(request: HttpRequest, payload: ProcedureInputSchema) -> tuple[HTTPStatus, ProcedureBaseOutputSchema]:
    service = CreateProcedureService()
    response: ProcedureBaseOutputSchema = service.execute(payload)

    return HTTPStatus.CREATED, response
