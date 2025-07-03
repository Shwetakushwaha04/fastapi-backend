import jwt

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta, timezone

from typing import Annotated

from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.exceptions import DoesNotExist

from models.user import User
from schemas.token import Token

SECRET_KEY = "2b11ce76e8b9394861be08e4a41cf0a94118fae732fad3e6567424b20961621b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 30 

router = APIRouter()

ph = PasswordHasher()

@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    
    try:
        user= await User.get(email=form_data.username )
        try:
            ph.verify(user.passwd, form_data.password)
            expire = datetime.now(timezone.utc) +timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            payload = {
                "sub": user.email,
                "name":user.name,
                "exp": expire
            }
            access_token = jwt.encode(payload, SECRET_KEY, algorithm= ALGORITHM)
            return Token(access_token = access_token, token_type= "bearer")
        except VerifyMismatchError:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
    except DoesNotExist:
        raise HTTPException( status_code=400, detail= "Incorrect username or password ")
    
AuthRouter = router
        