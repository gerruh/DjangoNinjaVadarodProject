from django.http import HttpRequest

from rest_api.doctor.schemas.input import DoctorPatchSchema
from rest_api.doctor.schemas.output import DoctorDetailOutputSchema
from rest_api.doctor.services.update_doctor_service import UpdateDoctorService


def patch_doctor_by_id(
    request: HttpRequest,
    doctor_id: int,
    payload: DoctorPatchSchema,
) -> DoctorDetailOutputSchema:
    service = UpdateDoctorService()
    doctor: DoctorDetailOutputSchema = service.execute(doctor_id, payload)

    return doctor
