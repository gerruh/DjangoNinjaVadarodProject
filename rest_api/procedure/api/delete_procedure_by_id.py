from django.http import HttpRequest

from rest_api.procedure.schemas.output import ProcedureDetailOutputSchema
from rest_api.procedure.services.delete_procedure_service import DeleteProcedureService


def delete_procedure_by_id(request: HttpRequest, procedure_id: int):
    service = DeleteProcedureService()
    procedure: ProcedureDetailOutputSchema = service.execute(procedure_id)
    return procedure
