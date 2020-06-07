from datetime import datetime
from typing import Optional, List

from pydantic.main import BaseModel

from user.schema import UserInResponse


class PostBase(BaseModel):
    title: str
    text: str
    date: datetime


class PostUpdate(PostBase):
    pass


class PostCreate(PostBase):
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True


class PostInDB(PostCreate):
    post_id: Optional[int]
    user: Optional[UserInResponse]


class PostCommentList(PostInDB):
    children: Optional[List[PostBase]] = []


class PostSingle(PostBase):
    post_id: Optional[int]
    user_id: str
