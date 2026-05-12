from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from django_ninja_project.medical_app.models import Procedure
from django_ninja_project.rest_api.procedure.exceptions import ProcedureAlreadyExistsException
from django_ninja_project.rest_api.procedure.schemas.input import ProcedurePatchSchema


def patch_procedure_by_id(request: HttpRequest, procedure_id: int, payload: ProcedurePatchSchema):
    procedure = get_object_or_404(Procedure, id=procedure_id)
    data = payload.model_dump(exclude_unset=True)

    if "name" in data:
        if Procedure.objects.exclude(id=procedure_id).filter(name=data["name"]).exists():
            raise ProcedureAlreadyExistsException(f'Процедура с именем {data["name"]} уже существует')

    for attr, value in data.items():
        setattr(procedure, attr, value)

    procedure.save()

    return procedure
