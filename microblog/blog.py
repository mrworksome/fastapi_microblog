from typing import List

from fastapi import APIRouter, Depends

from core.fast_users import fastapi_users
from microblog import service
from microblog.schema import PostCreate, PostList, PostSingle
from user.model import User

router = APIRouter()


@router.get('/', response_model=List[PostList])
async def post_list():
    return await service.get_post_list()


@router.post('/')
async def post_create(post: PostCreate, user: User = Depends(fastapi_users.get_current_user)):
    return await service.create_post(post, user)


@router.get('/{pk}', response_model=PostSingle)
async def post_list(pk: int):
    return await service.get_post(pk)
