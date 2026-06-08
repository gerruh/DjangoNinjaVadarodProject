from common.api.exceptions import AppException


def register_exception_handlers(api):
    @api.exception_handler(AppException)
    def handle_app_exception(request, exc):
        return api.create_response(
            request,
            {"detail": str(exc)},
            status=exc.status_code,
        )
