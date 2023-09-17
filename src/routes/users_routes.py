from typing import List

from fastapi import APIRouter

from src.models.user_model import UserOut, UserIn

router = APIRouter(
    prefix='/api/v1/users',
    tags=['Users']
)


@router.get(path='', response_model=List[UserOut])
async def find_all_users():
    return ''


@router.get(path="/{id}", response_model=UserOut)
async def find_user_by_id(id: int):
    return ''


@router.post(path='', response_model=UserOut)
async def create_user(user: UserIn):
    return ''


@router.put(path="/{id}", response_model=UserOut)
async def update_user(id: int, user: UserIn):
    return ''


@router.delete(path="/{id}", response_model=UserOut)
async def delete_visit(id: int):
    return ''
