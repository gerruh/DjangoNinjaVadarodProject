from datetime import datetime
from http import HTTPStatus

from django.http import HttpRequest

from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.exceptions import FacilityAlreadyExistsException
from django_ninja_project.rest_api.facility.schemas.input import FacilityInputSchema


def create_facility(request: HttpRequest, payload: FacilityInputSchema):
    if Facility.objects.filter(address=payload.address).exists():
        raise FacilityAlreadyExistsException(
            f"Facility with address {payload.address} already exists"
        )

    facility = Facility.objects.create(
        name=payload.name,
        address=payload.address,
        start_work_time=payload.start_work_time,
        end_work_time=payload.end_work_time,
        created_at=datetime.now(),
    )

    if payload.procedures:
        facility.procedures.set(payload.procedures)

    return HTTPStatus.CREATED, facility
