from http import HTTPStatus

from django.http import HttpRequest

from rest_api.doctor.schemas.input import DoctorInputSchema
from rest_api.doctor.schemas.output import DoctorBaseOutputSchema
from rest_api.doctor.services.create_doctor_service import CreateDoctorService


def create_doctor(request: HttpRequest, payload: DoctorInputSchema) -> tuple[HTTPStatus, DoctorBaseOutputSchema]:
    service = CreateDoctorService()
    response: DoctorBaseOutputSchema = service.execute(payload)

    return HTTPStatus.CREATED, response
