from django.http import HttpRequest

from rest_api.doctor.schemas.output import DoctorDetailOutputSchema
from rest_api.doctor.services.delete_doctor_service import DeleteDoctorService


def delete_doctor_by_id(request: HttpRequest, doctor_id: int) -> DoctorDetailOutputSchema:
    service = DeleteDoctorService()
    doctor: DoctorDetailOutputSchema = service.execute(doctor_id)

    return doctor
