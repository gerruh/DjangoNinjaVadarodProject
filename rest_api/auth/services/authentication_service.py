from django.contrib.auth import authenticate
from ninja_jwt.tokens import RefreshToken

from common.api.exceptions import UnauthorizedException
from rest_api.auth.schemas.input import AuthInputSchema
from rest_api.auth.schemas.output import AuthOutputSchema


class AuthService:

    @staticmethod
    def login(data: AuthInputSchema) -> AuthOutputSchema:
        user = authenticate(
            username=data.login,
            password=data.password,
        )

        if user is None:
            raise UnauthorizedException("User not found")

        refresh = RefreshToken.for_user(user)

        return AuthOutputSchema(
            # здесь ругается потому что access_token - динамическая переменная
            access_token=str(refresh.access_token),
            refresh_token=str(refresh),
        )