from http import HTTPStatus

from ninja import Router

from common.api.responses import ErrorResponse
from rest_api.user.api.create_user import create_user
from rest_api.user.schemas.output import UserOutputSchema

user_router = Router(tags=["User"])

user_router.add_api_operation(
    methods=['POST'],
    path='/',
    response={
        HTTPStatus.CREATED: UserOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse,
    },
    view_func=create_user,
    summary="Create User",
    auth=None
)