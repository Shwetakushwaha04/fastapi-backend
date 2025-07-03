from tortoise.contrib.pydantic import pydantic_model_creator

from models.user import User

UserPydantic = pydantic_model_creator(User, name="User", exclude=['passwd'])
UserSession = pydantic_model_creator(User, name="User", exclude=['passwd', 'todos'])
UserTempPydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)

class UserInPydantic(UserTempPydantic):
  passwd: str