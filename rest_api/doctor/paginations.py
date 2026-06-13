from common.api.paginations import GenericLimitOffsetPagination
from rest_api.doctor.schemas.output import DoctorListOutputSchema


class DoctorPagination(GenericLimitOffsetPagination[DoctorListOutputSchema]):...
