from django.http import HttpRequest

from rest_api.auth.schemas.input import RefreshInputSchema
from rest_api.auth.schemas.output import LoginOutputSchema
from rest_api.auth.services.session_service import SessionService
from rest_api.auth.services.token_service import TokenService


def refresh_user_token(request: HttpRequest, payload: RefreshInputSchema) -> LoginOutputSchema:
    token_service: TokenService = TokenService()
    session_service: SessionService = SessionService(token_service)
    response: LoginOutputSchema = session_service.refresh(payload.refresh_token)
    return response