from typing import Any

from ninja import NinjaAPI
from ninja.errors import ValidationError as NinjaValidationError

from common.api.exceptions import AppException


def _normalize_validation_errors(errors: list[dict[str, Any]]) -> list[dict[str, str]]:
    normalized_errors: list[dict[str, str]] = []
    ignored_locations = {"body", "query", "path", "form"}

    for error in errors:
        location_parts = [
            str(part)
            for part in error.get("loc", [])
            if part not in ignored_locations
        ]
        normalized_errors.append(
            {
                "field": ".".join(location_parts) or "request",
                "message": str(error.get("msg", "Invalid value")),
            }
        )

    return normalized_errors


def register_exception_handlers(api: NinjaAPI) -> None:
    @api.exception_handler(AppException)
    def handle_app_exception(request, exc):
        return api.create_response(
            request,
            {"detail": str(exc)},
            status=exc.status_code,
        )

    @api.exception_handler(NinjaValidationError)
    def handle_validation_error(request, exc: NinjaValidationError):
        return api.create_response(
            request,
            {
                "detail": "Validation error",
                "errors": _normalize_validation_errors(exc.errors),
            },
            status=400,
        )
