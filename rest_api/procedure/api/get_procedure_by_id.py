from django.http import HttpRequest

from apps.procedure.models import Procedure
from common.api.exceptions import NotFoundException


def get_procedure_by_id(request: HttpRequest, procedure_id: int):
    try:
        procedure = Procedure.objects.get(id=procedure_id)
    except Procedure.DoesNotExist:
        raise NotFoundException(f'Procedure with id {procedure_id} does not exist')

    return procedure
