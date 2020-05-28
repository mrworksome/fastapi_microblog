from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db_utils import database
from user.model import User
from user.schema import UserDB

users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "dhfg67ewtf8wgf6ewgc8y28g8q893hc7808fwh7w4bynw74y7"

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=3600),
]
