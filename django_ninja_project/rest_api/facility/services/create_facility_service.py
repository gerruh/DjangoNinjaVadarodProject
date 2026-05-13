from sqlite3 import IntegrityError

from django.db import transaction

from django_ninja_project.common.api.exceptions import AlreadyExistsException, AppException, NotFoundException
from django_ninja_project.medical_app.models import Facility, Procedure
from django_ninja_project.rest_api.facility.schemas.input import FacilityInputSchema
from django_ninja_project.rest_api.facility.schemas.output import FacilityBaseOutputSchema


class CreateFacilityService:
    @transaction.atomic
    def execute(self, payload: FacilityInputSchema) -> FacilityBaseOutputSchema:

        # Тут на unqiue constraint будет 500 т.к. констрейнты в склайт чекаются в конце атомика соответственно интегрити еррор тупо не отловится
        try:
            facility: Facility = Facility.objects.create(
                **payload.model_dump(exclude={"procedures"})
            )
        except IntegrityError:
            raise AlreadyExistsException(
                f"Facility with such {payload.name} and {payload.address} combination already exists"
            )

        procedures = Procedure.objects.filter(id__in=payload.procedures)

        if len(procedures) != len(payload.procedures):
            raise NotFoundException(f"Invalid procedure references with ids: {payload.procedures}")

        facility.procedures.add(*payload.procedures)

        return FacilityBaseOutputSchema.model_validate(facility)
