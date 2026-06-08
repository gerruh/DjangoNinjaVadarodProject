from http import HTTPStatus

from django.http import HttpRequest

from rest_api.facility.schemas.input import FacilityInputSchema
from rest_api.facility.schemas.output import FacilityBaseOutputSchema
from rest_api.facility.services.create_facility_service import CreateFacilityService


def create_facility(request: HttpRequest, payload: FacilityInputSchema) -> tuple[HTTPStatus, FacilityBaseOutputSchema]:
    service = CreateFacilityService()
    response: FacilityBaseOutputSchema = service.execute(payload)

    return HTTPStatus.CREATED, response
