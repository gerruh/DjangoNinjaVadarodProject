from django.http import HttpRequest

from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.exceptions import FacilityNotFoundException


def get_facility_by_id(request: HttpRequest, facility_id: int):
    facility = Facility.objects.filter(
        id=facility_id,
        deleted_at__isnull=True,
    ).first()

    if facility is None:
        raise FacilityNotFoundException(f"Учреждение с id {facility_id} не найден")

    return facility
