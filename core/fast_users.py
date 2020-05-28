from fastapi_users import FastAPIUsers
from starlette.requests import Request

from user.logic import user_db, auth_backends, SECRET
from user.schema import UserCreate, UserUpdate, UserDB, User

fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
    SECRET,
)


@fastapi_users.on_after_register()
def on_after_register(user: User, request: Request):
    print(f"User {user.id} has registered.")


@fastapi_users.on_after_forgot_password()
def on_after_forgot_password(user: User, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")
