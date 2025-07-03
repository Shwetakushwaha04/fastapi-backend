import jwt
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from models.user import User
from schemas.user import UserSession

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "2b11ce76e8b9394861be08e4a41cf0a94118fae732fad3e6567424b20961621b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")
    if email is None:
      raise credentials_exception
    user = await UserSession.from_queryset_single(User.get(email=email))
    return user
  except InvalidTokenError:
    raise credentials_exception

gcu = Annotated[UserSession, Depends(get_current_user)]