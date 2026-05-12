from django.http import HttpRequest

from django_ninja_project.medical_app.models import Procedure
from django_ninja_project.rest_api.procedure.exceptions import ProcedureAlreadyExistsException
from django_ninja_project.rest_api.procedure.schemas.input import ProcedureInputSchema


def create_procedure(request: HttpRequest, payload: ProcedureInputSchema):
    if Procedure.objects.filter(name=payload.name).exists():
        raise ProcedureAlreadyExistsException(f'Procedure {payload.name} already exists')

    procedure = Procedure.objects.create(
        name=payload.name,
        type=payload.type,
        cost=payload.cost
    )

    return procedure
