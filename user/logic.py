from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from starlette.requests import Request

from core.db_utils import database
from user.model import User
from user.schema import UserDB

users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "dhfg67ewtf8wgf6ewgc8y28g8q893hc7808fwh7w4bynw74y7"

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)


# auth_backends = [
#     JWTAuthentication(secret=SECRET, lifetime_seconds=3600),
# ]


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")
