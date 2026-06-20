from http import HTTPStatus

from django.http import HttpRequest

from rest_api.user.schemas.input import UserInputSchema
from rest_api.user.schemas.output import UserOutputSchema
from rest_api.user.services.create_user_service import CreateUserService


def create_user(request: HttpRequest, payload: UserInputSchema) -> tuple[HTTPStatus, UserOutputSchema]:
    service = CreateUserService()
    response: UserOutputSchema = service.execute(payload)

    return HTTPStatus.CREATED, response