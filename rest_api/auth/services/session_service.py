from rest_api.auth.schemas.output import LoginOutputSchema
from rest_api.auth.services.token_service import TokenService


class SessionService:

    def __init__(self, token_service: TokenService) -> None:
        self.token_service = token_service

    def refresh(self, refresh_token: str) -> LoginOutputSchema:
        response = self.token_service.rotate(refresh_token)
        return LoginOutputSchema(**response)

    def logout(self, refresh_token: str) -> None:
        self.token_service.revoke(refresh_token)
