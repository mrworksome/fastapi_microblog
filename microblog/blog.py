from typing import List

from fastapi import APIRouter, Depends, HTTPException

from core.fast_users import fastapi_users
from microblog import service
from microblog.schema import PostCreate, PostCommentList, PostSingle, PostUpdate, PostInDB
from user.model import User

router = APIRouter()


@router.get('/', response_model=List[PostSingle])
async def get_all_post():
    return await service.get_post_list()


@router.post('/', status_code=201, response_model=PostInDB)
async def post_create(
        post: PostCreate,
        user: User = Depends(fastapi_users.get_current_user)):
    return await service.create_post(post, user)


@router.get('/{pk}', response_model=PostCommentList)
async def get_post_with_children(pk: int):
    post = await service.get_post(pk)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{pk}", status_code=201, response_model=PostInDB)
async def post_update(
        pk: int, item: PostUpdate,
        user: User = Depends(fastapi_users.get_current_active_user)):
    return await service.update_post(pk, item, user)


@router.delete("/{pk}", status_code=204)
async def post_delete(
        pk: int,
        user: User = Depends(fastapi_users.get_current_active_user)):
    return await service.delete_post(pk, user)
