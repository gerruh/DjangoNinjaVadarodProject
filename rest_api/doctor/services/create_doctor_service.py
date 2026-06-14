from typing import Any

from django.db import IntegrityError, transaction

from apps.doctor.models import Doctor
from apps.facility.models import Facility
from common.api.exceptions import AlreadyExistsException, NotFoundException
from rest_api.doctor.schemas.input import DoctorInputSchema
from rest_api.doctor.schemas.output import DoctorBaseOutputSchema


class CreateDoctorService:
    @transaction.atomic
    def execute(self, payload: DoctorInputSchema) -> DoctorBaseOutputSchema:
        if not Facility.objects.filter(id=payload.facility, deleted_at__isnull=True).exists():
            raise NotFoundException(f"Facility with id {payload.facility} does not exist")

        data: dict[str, Any] = payload.model_dump()
        facility_id = data.pop("facility")

        try:
            doctor: Doctor = Doctor.objects.create(
                **data,
                facility_id=facility_id,
            )
        except IntegrityError:
            raise AlreadyExistsException(f'Doctor with name {payload.name} and speciality {payload.speciality} already exists')

        return DoctorBaseOutputSchema.model_validate(doctor)
