from django.http import HttpRequest

from rest_api.procedure.schemas.input import ProcedurePatchSchema
from rest_api.procedure.schemas.output import ProcedureDetailOutputSchema
from rest_api.procedure.services.update_procedure_service import UpdateProcedureService


def patch_procedure_by_id(request: HttpRequest, procedure_id: int, payload: ProcedurePatchSchema):
    service = UpdateProcedureService()
    procedure: ProcedureDetailOutputSchema = service.execute(procedure_id, payload)
    return procedure
