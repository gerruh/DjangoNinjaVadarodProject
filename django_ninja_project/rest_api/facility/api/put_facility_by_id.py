from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.exceptions import FacilityAlreadyExistsException
from django_ninja_project.rest_api.facility.schemas.input import FacilityInputSchema


def put_facility_by_id(request: HttpRequest, facility_id: int, payload: FacilityInputSchema):
    facility = get_object_or_404(Facility, id=facility_id)
    data = payload.model_dump()
    procedures = data.pop("procedures", None)

    if Facility.objects.exclude(id=facility_id).filter(address=data["address"]).exists():
        raise FacilityAlreadyExistsException(f'Учреждение с адресом {data["address"]} уже существует')

    for attr, value in data.items():
        setattr(facility, attr, value)

    facility.save()
    facility.procedures.set(procedures)

    return facility
