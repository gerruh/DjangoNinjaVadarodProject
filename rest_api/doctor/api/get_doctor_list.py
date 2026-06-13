from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate
from ninja_extra.ordering import Ordering, ordering

from apps.doctor.models import Doctor
from rest_api.doctor.paginations import DoctorPagination
from rest_api.doctor.schemas.filter import DoctorFilterSchema


@paginate(DoctorPagination)
@ordering(
    Ordering,
    ordering_fields=["id", "name", "speciality", "is_active"],
)
def get_doctor_list(request: HttpRequest, filters: DoctorFilterSchema = Query()) -> QuerySet[Doctor]:
    return filters.filter(Doctor.objects.filter(deleted_at__isnull=True))
