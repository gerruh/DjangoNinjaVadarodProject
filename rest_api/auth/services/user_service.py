from django.contrib.auth import authenticate
from apps.user.models import User
from common.api.exceptions import UnauthorizedException, AlreadyExistsException
from rest_api.auth.schemas.input import LoginInputSchema, RegisterInputSchema
from rest_api.auth.schemas.output import LoginOutputSchema, RegisterOutputSchema
from rest_api.auth.services.token_service import TokenService


class UserService:

    def __init__(self, token_service: TokenService):
        self.token_service = token_service

    def register(self, payload: RegisterInputSchema) -> RegisterOutputSchema:
        if User.objects.filter(email=payload.email).exists():
            raise AlreadyExistsException(f'User with email {payload.email} already exists')

        user = User.objects.create_user(
            email=payload.email,
            password=payload.password,
        )

        tokens: dict[str, str] = self.token_service.issue(user)

        return RegisterOutputSchema(**tokens)

    def login(self, payload: LoginInputSchema) -> LoginOutputSchema:
        user = authenticate(
            email=payload.email,
            password=payload.password,
        )

        if user is None:
            raise UnauthorizedException("User not authorized")

        tokens: dict[str, str] = self.token_service.issue(user)
        return LoginOutputSchema(**tokens)
