from argon2 import PasswordHasher
from typing import List
from fastapi import APIRouter

from models.user import User
from schemas.user import UserInPydantic, UserPydantic 

router = APIRouter()

ph = PasswordHasher()

@router.get("", response_model= List[UserPydantic])
async def get_users():
    return await UserPydantic.from_queryset(User.all())

@router.post("", response_model= UserPydantic)
async def add_user(user: UserInPydantic):
    user_obj = await User.create(name= user.name, email= user.email, passwd= ph.hash(user.passwd))
    return await UserPydantic.from_tortoise_orm(user_obj)

UserRouter = router
