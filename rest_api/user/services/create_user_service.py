from django.db import transaction

from apps.user.models import User
from common.api.exceptions import AlreadyExistsException
from rest_api.user.schemas.input import UserInputSchema
from rest_api.user.schemas.output import UserOutputSchema


class CreateUserService:
    @transaction.atomic
    def execute(self, payload: UserInputSchema) -> UserOutputSchema:
        if User.objects.filter(email=payload.email).exists():
            raise AlreadyExistsException(f'User with email {payload.email} already exists')

        user = User.objects.create_user(
            email=payload.email,
            password=payload.password,
        )

        return UserOutputSchema.model_validate(user)
