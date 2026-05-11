from django_ninja_project.common.api.exceptions import AppException


class FacilityAlreadyExistsException(AppException):
    status_code = 409
    code = "FACILITY_ALREADY_EXISTS"


class FacilityNotFoundException(AppException):
    status_code = 404
    code = "FACILITY_NOT_FOUND"
