from fastapi_users import FastAPIUsers

from user.logic import user_db, jwt_authentication
from user.schema import UserCreate, UserUpdate, UserDB, User

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB
)
