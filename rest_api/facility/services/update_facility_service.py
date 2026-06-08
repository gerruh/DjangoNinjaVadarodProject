from typing import Any

from django.db import transaction, IntegrityError

from common.api.exceptions import NotFoundException, AlreadyExistsException
from apps.facility.models import Facility
from rest_api.facility.schemas.input import FacilityInputSchema
from rest_api.facility.schemas.output import FacilityDetailOutputSchema


class UpdateFacilityService:
    @transaction.atomic
    def execute(self, facility_id: int, payload: FacilityInputSchema) -> FacilityDetailOutputSchema:
        try:
            facility: Facility = Facility.objects.prefetch_related("procedures").get(id=facility_id)
        except Facility.DoesNotExist:
            raise NotFoundException(f"Facility with id {facility_id} does not exist")

        data: dict[str, Any] = payload.model_dump(exclude_unset=True)
        procedures: list[int] = data.pop("procedures", None)

        try:
            for attr, value in data.items():
                setattr(facility, attr, value)
        except IntegrityError:
            raise AlreadyExistsException(
                f"Facility with such {payload.name} and {payload.address} combination already exists")

        facility.save()

        if procedures is not None:
            facility.procedures.set(procedures)
            facility.refresh_from_db()

        return FacilityDetailOutputSchema.model_validate(facility)
