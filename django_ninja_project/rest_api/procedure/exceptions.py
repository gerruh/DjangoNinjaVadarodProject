from django_ninja_project.common.api.exceptions import AppException


class ProcedureAlreadyExistsException(AppException):
    status_code = 409
    code = "PROCEDURE_ALREADY_EXISTS"


class ProcedureNotFoundException(AppException):
    status_code = 404
    code = "PROCEDURE_NOT_FOUND"
