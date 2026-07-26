from django.http import HttpRequest

from rest_api.auth.schemas.input import LoginInputSchema
from rest_api.auth.schemas.output import LoginOutputSchema
from rest_api.auth.services.token_service import TokenService
from rest_api.auth.services.user_service import UserService


def login_user(request: HttpRequest, payload: LoginInputSchema) -> LoginOutputSchema:
    token_service: TokenService = TokenService()
    user_service: UserService = UserService(token_service)
    response: LoginOutputSchema = user_service.login(payload)

    return response