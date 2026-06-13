from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate
from ninja_extra.ordering import Ordering, ordering

from apps.procedure.models import Procedure
from rest_api.procedure.filters import ProcedureFilterSchema
from rest_api.procedure.paginations import ProcedurePagination


@paginate(ProcedurePagination)
@ordering(
    Ordering,
    ordering_fields=["id", "name", "cost"]
)
def get_procedure_list(request: HttpRequest, filters: ProcedureFilterSchema = Query()) -> Query:
    return filters.filter(Procedure.objects.filter(deleted_at__isnull=True))
