from typing import Any

from django.db import IntegrityError, transaction

from common.api.exceptions import NotFoundException, AlreadyExistsException
from apps.facility.models import Facility
from rest_api.facility.schemas.input import FacilityInputSchema
from rest_api.facility.schemas.output import FacilityDetailOutputSchema


class UpdateFacilityService:
    @transaction.atomic
    def execute(self, facility_id: int, payload: FacilityInputSchema) -> FacilityDetailOutputSchema:
        try:
            facility: Facility = Facility.objects.prefetch_related("procedures").get(id=facility_id, deleted_at__isnull=True)
        except Facility.DoesNotExist:
            raise NotFoundException(f"Facility with id {facility_id} does not exist")

        data: dict[str, Any] = payload.model_dump(exclude_unset=True)
        procedures: list[int] = data.pop("procedures", None)

        for attr, value in data.items():
            setattr(facility, attr, value)

        try:
            facility.save()
        except IntegrityError:
            raise AlreadyExistsException(
                f"Facility with such {facility.name} and {facility.address} combination already exists"
            )

        if procedures is not None:
            facility.procedures.set(procedures)
            facility.refresh_from_db()

        return FacilityDetailOutputSchema.model_validate(facility)
