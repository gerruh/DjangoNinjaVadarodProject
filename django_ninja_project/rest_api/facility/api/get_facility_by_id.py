from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404

from django_ninja_project.common.api.exceptions import NotFoundException
from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.schemas.output import FacilityDetailOutputSchema


def get_facility_by_id(request: HttpRequest, facility_id: int):
    try:
        facility = Facility.objects.get(id=facility_id)
    except Facility.DoesNotExist:
        raise NotFoundException(f"Facility with id {facility_id} is not found.")

    return FacilityDetailOutputSchema.model_validate(facility)
