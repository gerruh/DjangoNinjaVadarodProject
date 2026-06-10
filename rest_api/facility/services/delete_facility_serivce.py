import datetime

from django.db import transaction

from common.api.exceptions import NotFoundException
from apps.facility.models import Facility
from rest_api.facility.schemas.output import FacilityDetailOutputSchema


class DeleteFacilityService:
    @transaction.atomic
    def execute(self, facility_id: int) -> FacilityDetailOutputSchema:
        try:
            facility: Facility = Facility.objects.get(id=facility_id, deleted_at__isnull=True)
        except Facility.DoesNotExist:
            raise NotFoundException(f"Facility with id {facility_id} not found")

        facility.deleted_at = datetime.datetime.now(datetime.timezone.utc)
        facility.save()

        return FacilityDetailOutputSchema.model_validate(facility)
