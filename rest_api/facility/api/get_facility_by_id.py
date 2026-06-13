from django.http import HttpRequest
from django.db.models import Prefetch

from common.api.exceptions import NotFoundException
from apps.facility.models import Facility
from apps.procedure.models import Procedure
from rest_api.facility.schemas.output import FacilityDetailOutputSchema


def get_facility_by_id(request: HttpRequest, facility_id: int) -> FacilityDetailOutputSchema:
    try:
        facility: Facility = Facility.objects.prefetch_related(
            Prefetch("procedures", queryset=Procedure.objects.filter(deleted_at__isnull=True)),
        ).get(id=facility_id, deleted_at__isnull=True)
    except Facility.DoesNotExist:
        raise NotFoundException(f"Facility with id {facility_id} is not found.")

    return FacilityDetailOutputSchema.model_validate(facility)
