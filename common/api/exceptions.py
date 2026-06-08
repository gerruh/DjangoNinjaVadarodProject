class AppException(Exception):
    status_code = 400
    default_detail = "Application exception"

    def __init__(self, detail: str | None = None):
        self.detail = detail or self.default_detail
        super().__init__(self.detail)

class NotFoundException(AppException):
    status_code = 404
    default_detail = "Object not found"

class AlreadyExistsException(AppException):
    status_code = 409
    default_detail = "Object already exists"