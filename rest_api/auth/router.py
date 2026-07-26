from http import HTTPStatus

from ninja import Router

from common.api.responses import ErrorResponse
from rest_api.auth.api.login_user import login_user
from rest_api.auth.api.logout_user import logout_user
from rest_api.auth.api.refresh_user_token import refresh_user_token
from rest_api.auth.api.register_user import register_user
from rest_api.auth.schemas.output import RegisterOutputSchema, LoginOutputSchema, RefreshOutputSchema

auth_router = Router(tags=["Auth"])

auth_router.add_api_operation(
    methods=['POST'],
    path='/register',
    response={
        HTTPStatus.CREATED: RegisterOutputSchema,
        HTTPStatus.CONFLICT: ErrorResponse
    },
    view_func=register_user,
    summary="Register user and return refresh & access token pair",
)

auth_router.add_api_operation(
    methods=['POST'],
    path='/login',
    response={
        HTTPStatus.OK: LoginOutputSchema,
        HTTPStatus.UNAUTHORIZED: ErrorResponse
    },
    view_func=login_user,
    summary="Login user",
)

auth_router.add_api_operation(
    methods=['POST'],
    path='/logout',
    response={
        HTTPStatus.OK: None,
        HTTPStatus.UNAUTHORIZED: ErrorResponse
    },
    view_func=logout_user,
    summary="Logout user and blacklist his refresh token",
)

auth_router.add_api_operation(
    methods=['POST'],
    path='/refresh',
    response={
        HTTPStatus.OK: RefreshOutputSchema,
        HTTPStatus.UNAUTHORIZED: ErrorResponse
    },
    view_func=refresh_user_token,
    summary="Refresh user token and blacklist his old refresh token",
)