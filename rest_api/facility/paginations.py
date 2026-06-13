from common.api.paginations import GenericLimitOffsetPagination
from rest_api.facility.schemas.output import FacilityListOutputSchema


class FacilityPagination(GenericLimitOffsetPagination[FacilityListOutputSchema] ):...