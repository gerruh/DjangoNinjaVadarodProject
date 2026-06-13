import datetime

from apps.doctor.models import Doctor
from common.api.exceptions import NotFoundException
from rest_api.doctor.schemas.output import DoctorDetailOutputSchema


class DeleteDoctorService:
    def execute(self, doctor_id: int) -> DoctorDetailOutputSchema:
        try:
            doctor: Doctor = Doctor.objects.get(id=doctor_id, deleted_at__isnull=True)
        except Doctor.DoesNotExist:
            raise NotFoundException(f"Doctor with id {doctor_id} not found")

        doctor.deleted_at = datetime.datetime.now(datetime.timezone.utc)
        doctor.save()

        return DoctorDetailOutputSchema.model_validate(doctor)
