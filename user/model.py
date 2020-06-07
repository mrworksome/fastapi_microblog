from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String

from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
