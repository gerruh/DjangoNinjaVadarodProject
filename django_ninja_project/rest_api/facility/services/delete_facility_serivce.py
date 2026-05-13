import datetime

from django.db import transaction

from django_ninja_project.common.api.exceptions import NotFoundException
from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.schemas.output import FacilityDetailOutputSchema


class DeleteFacilityService:
    @transaction.atomic
    def execute(self, facility_id: int) -> FacilityDetailOutputSchema:
        try:
            facility: Facility = Facility.objects.get(id=facility_id)
        except Facility.DoesNotExist:
            raise NotFoundException(f"Facility with id {facility_id} not found")

        facility.deleted_at = datetime.timezone()
        facility.save()

        return FacilityDetailOutputSchema.model_validate(facility)
