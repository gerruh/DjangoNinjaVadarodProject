from datetime import datetime

from django.http import HttpRequest

from apps.procedure.models import Procedure
from rest_api.procedure.exceptions import ProcedureNotFoundException


def delete_procedure_by_id(request: HttpRequest, procedure_id: int):

    try:
        procedure = Procedure.objects.get(id=procedure_id)
    except Procedure.DoesNotExist:
        raise ProcedureNotFoundException(f"Учреждение с id {procedure_id} не найден")

    procedure.deleted_at = datetime.now()
    procedure.save()

    return procedure
