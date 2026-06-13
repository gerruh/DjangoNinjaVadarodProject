from django.http import HttpRequest

from apps.doctor.models import Doctor
from common.api.exceptions import NotFoundException
from rest_api.doctor.schemas.output import DoctorDetailOutputSchema


def get_doctor_by_id(request: HttpRequest, doctor_id: int) -> DoctorDetailOutputSchema:
    try:
        doctor: Doctor = Doctor.objects.select_related("facility").get(
            id=doctor_id,
            deleted_at__isnull=True,
        )
    except Doctor.DoesNotExist:
        raise NotFoundException(f"Doctor with id {doctor_id} does not exist")

    return DoctorDetailOutputSchema.model_validate(doctor)
