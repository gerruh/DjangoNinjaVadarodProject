from django.http import HttpRequest

from common.api.exceptions import NotFoundException
from apps.facility.models import Facility
from rest_api.facility.schemas.output import FacilityDetailOutputSchema


def get_facility_by_id(request: HttpRequest, facility_id: int):
    try:
        facility = Facility.objects.get(id=facility_id, deleted_at__isnull=True)
    except Facility.DoesNotExist:
        raise NotFoundException(f"Facility with id {facility_id} is not found.")

    return FacilityDetailOutputSchema.model_validate(facility)
