from django.http import HttpRequest

from django_ninja_project.rest_api.facility.schemas.input import FacilityPatchSchema
from django_ninja_project.rest_api.facility.schemas.output import FacilityDetailOutputSchema
from django_ninja_project.rest_api.facility.services.update_facility_service import UpdateFacilityService


def patch_facility_by_id(request: HttpRequest, facility_id: int,
                         payload: FacilityPatchSchema) -> FacilityDetailOutputSchema:
    service = UpdateFacilityService()
    facility: FacilityDetailOutputSchema = service.execute(facility_id=facility_id, payload=payload)

    return facility
