from django.http import HttpRequest
from ninja import Query
from ninja.pagination import paginate

from django_ninja_project.medical_app.models import Facility
from django_ninja_project.rest_api.facility.schemas.filter import FacilityFilterSchema
from django_ninja_project.rest_api.facility.schemas.output import FacilityOutputSchema


@paginate
def get_facility_list(request: HttpRequest, filters: FacilityFilterSchema = Query()) -> list[FacilityOutputSchema]:
    return [FacilityOutputSchema.model_validate(obj) for obj in filters.filter(Facility.objects.all())]
