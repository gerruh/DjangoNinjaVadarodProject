from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate
from ninja_extra.ordering import ordering, Ordering

from apps.facility.models import Facility
from rest_api.facility.filters import FacilityFilterSchema
from rest_api.facility.paginations import FacilityPagination


@paginate(FacilityPagination)
@ordering(
    Ordering,
    ordering_fields = ["id", "name", "address", "start_work_time", "end_work_time"]
)
def get_facility_list(request: HttpRequest, filters: FacilityFilterSchema = Query()) -> Query:
    return filters.filter(Facility.objects.filter(deleted_at__isnull=True))
