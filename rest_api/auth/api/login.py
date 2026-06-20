from django.http import HttpRequest

from rest_api.auth.schemas.input import AuthInputSchema
from rest_api.auth.schemas.output import AuthOutputSchema
from rest_api.auth.services.authentication_service import AuthService


def login(request: HttpRequest, payload: AuthInputSchema) -> AuthOutputSchema:
    service = AuthService()
    response = service.login(payload)

    return AuthOutputSchema.model_validate(response)