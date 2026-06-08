from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate

from apps.facility.models import Facility
from rest_api.facility.schemas.filter import FacilityFilterSchema


@paginate
def get_facility_list(request: HttpRequest, filters: FacilityFilterSchema = Query()) -> Query:
    return filters.filter(Facility.objects.filter(deleted_at__isnull=True))
