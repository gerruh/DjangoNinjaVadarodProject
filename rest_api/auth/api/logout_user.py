from django.http import HttpRequest

from rest_api.auth.services.session_service import SessionService
from rest_api.auth.services.token_service import TokenService


def logout_user(request: HttpRequest, refresh_token: str):
    token_service: TokenService = TokenService()
    service: SessionService = SessionService(token_service)
    service.logout(refresh_token)