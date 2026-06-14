from sqlite3 import IntegrityError
from common.api.exceptions import AlreadyExistsException, NotFoundException
from apps.facility.models import Facility
from apps.facility.models import Procedure
from rest_api.facility.schemas.input import FacilityInputSchema
from rest_api.facility.schemas.output import FacilityBaseOutputSchema


from django.db import transaction, IntegrityError

class CreateFacilityService:
    @transaction.atomic
    def execute(self, payload: FacilityInputSchema) -> FacilityBaseOutputSchema:

        if Facility.objects.filter(
            name=payload.name,
            address=payload.address
        ).exists():
            raise AlreadyExistsException(
                f"Facility with name {payload.name} and address {payload.address} already exists"
            )

        procedures_qs = Procedure.objects.filter(id__in=payload.procedures)

        existing_ids = set(procedures_qs.values_list("id", flat=True))
        missing_ids = set(payload.procedures) - existing_ids

        if missing_ids:
            raise NotFoundException(
                f"Invalid procedure references with ids: {list(missing_ids)}"
            )

        try:
            facility = Facility.objects.create(
                **payload.model_dump(exclude={"procedures"})
            )
        except IntegrityError:
            raise AlreadyExistsException(
                "Facility with such name and address already exists"
            )

        facility.procedures.add(*procedures_qs)

        return FacilityBaseOutputSchema.model_validate(facility)
