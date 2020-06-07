from fastapi import APIRouter

from core.fast_users import fastapi_users
from user.logic import jwt_authentication, on_after_register, SECRET, on_after_forgot_password

routes = APIRouter()

routes.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"])

routes.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)

routes.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
routes.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
