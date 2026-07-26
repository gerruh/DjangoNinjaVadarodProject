from http import HTTPStatus

from django.http import HttpRequest

from rest_api.auth.schemas.input import RegisterInputSchema
from rest_api.auth.schemas.output import RegisterOutputSchema
from rest_api.auth.services.user_service import UserService
from rest_api.auth.services.token_service import TokenService


def register_user(request: HttpRequest, payload: RegisterInputSchema) -> tuple[HTTPStatus, RegisterOutputSchema]:
    service: UserService = UserService(TokenService())
    response: RegisterOutputSchema = service.register(payload)
    return HTTPStatus.CREATED, response