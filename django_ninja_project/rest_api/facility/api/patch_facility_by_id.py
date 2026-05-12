from django.http import HttpRequest

from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.exceptions import FacilityAlreadyExistsException, FacilityNotFoundException
from django_ninja_project.rest_api.facility.schemas.input import FacilityPatchSchema


def patch_facility_by_id(request: HttpRequest, facility_id: int, payload: FacilityPatchSchema):
    try:
        facility = Facility.objects.get(id=facility_id)
    except Facility.DoesNotExist:
        raise FacilityNotFoundException(f"Учреждение с id {facility_id} не найден")

    data = payload.model_dump(exclude_unset=True)

    procedures = data.pop("procedures", None)

    if "address" in data:
        if Facility.objects.exclude(id=facility_id).filter(address=data["address"]).exists():
            raise FacilityAlreadyExistsException(f'Учреждение с адресом {data["address"]} уже существует')

    for attr, value in data.items():
        setattr(facility, attr, value)

    facility.save()

    if procedures is not None:
        facility.procedures.set(procedures)

    return facility
