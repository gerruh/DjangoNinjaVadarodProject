from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate

from apps.procedure.models import Procedure
from rest_api.procedure.schemas.filter import ProcedureFilterSchema


@paginate
def get_procedure_list(request: HttpRequest, filters: ProcedureFilterSchema = Query()) -> Query:
    return filters.filter(Procedure.objects.filter(deleted_at__isnull=True))
