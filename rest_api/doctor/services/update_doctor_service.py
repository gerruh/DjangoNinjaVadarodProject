from typing import Any

from django.db import IntegrityError, transaction

from apps.doctor.models import Doctor
from apps.facility.models import Facility
from common.api.exceptions import AlreadyExistsException, NotFoundException
from rest_api.doctor.schemas.input import DoctorPatchSchema
from rest_api.doctor.schemas.output import DoctorDetailOutputSchema


class UpdateDoctorService:
    @transaction.atomic
    def execute(self, doctor_id: int, payload: DoctorPatchSchema) -> DoctorDetailOutputSchema:
        try:
            doctor: Doctor = Doctor.objects.get(id=doctor_id, deleted_at__isnull=True)
        except Doctor.DoesNotExist:
            raise NotFoundException(f"Doctor with id {doctor_id} does not exist")

        data: dict[str, Any] = payload.model_dump(exclude_unset=True)

        if "facility" in data:
            facility_id: int | None = data.pop("facility")
            if facility_id is not None and not Facility.objects.filter(
                id=facility_id,
                deleted_at__isnull=True,
            ).exists():
                raise NotFoundException(f"Facility with id {facility_id} does not exist")
            doctor.facility_id = facility_id

        for attr, value in data.items():
            setattr(doctor, attr, value)

        try:
            doctor.save()
        except IntegrityError:
            raise AlreadyExistsException("Doctor with such data already exists")

        return DoctorDetailOutputSchema.model_validate(doctor)
