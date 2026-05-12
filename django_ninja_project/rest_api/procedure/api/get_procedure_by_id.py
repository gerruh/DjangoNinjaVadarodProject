from django.http import HttpRequest

from django_ninja_project.medical_app.models import Procedure
from django_ninja_project.rest_api.procedure.exceptions import ProcedureNotFoundException


def get_procedure_by_id(request: HttpRequest, procedure_id: int):
    try:
        procedure = Procedure.objects.get(id=procedure_id)
    except Procedure.DoesNotExist:
        raise ProcedureNotFoundException(f'Procedure with id {procedure_id} does not exist')

    return procedure
