from django.http import HttpRequest

from rest_api.facility.schemas.output import FacilityDetailOutputSchema
from rest_api.facility.services.delete_facility_serivce import DeleteFacilityService


def delete_facility_by_id(request: HttpRequest, facility_id: int) -> FacilityDetailOutputSchema:
    service = DeleteFacilityService()
    facility: FacilityDetailOutputSchema = service.execute(facility_id=facility_id)

    return facility
