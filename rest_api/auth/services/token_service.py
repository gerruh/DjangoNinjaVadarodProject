from django.contrib.auth.base_user import AbstractBaseUser
from ninja_jwt.exceptions import TokenError
from ninja_jwt.tokens import RefreshToken

from apps.user.models import User
from common.api.exceptions import UnauthorizedException


class TokenService:
    @staticmethod
    # здесь ругается потому что access_token - динамическая переменная
    def issue(user: AbstractBaseUser) -> dict[str, str]:
        refresh = RefreshToken.for_user(user)

        return {"access_token": str(refresh.access_token), "refresh_token": str(refresh)}

    @staticmethod
    def rotate(refresh_token: str) -> dict[str, str]:
        """
        Инвалидирует старый refresh
        и выдает новую пару access + refresh
        """

        try:
            old_refresh = RefreshToken(refresh_token)

        except TokenError:
            raise UnauthorizedException("Invalid refresh token")

        # достаем пользователя из payload
        user_id = old_refresh["user_id"]

        user = User.objects.get(id=user_id)

        # убиваем старый refresh
        old_refresh.blacklist()

        # создаем новый
        new_refresh = RefreshToken.for_user(user)

        return {"access_token": str(new_refresh.access_token), "refresh_token": str(new_refresh)}

    @staticmethod
    def revoke(refresh_token: str) -> None:
        try:
            old_refresh = RefreshToken(refresh_token)

        except TokenError:
            raise UnauthorizedException("Invalid refresh token")

        old_refresh.blacklist()
