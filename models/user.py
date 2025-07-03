from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20, null=False)
    email = fields.CharField(max_length=50, unique=True)
    passwd = fields.CharField(max_length=128, null=False)

    class PydanticMeta:
        exclude = ["passwd"]  # Exclude password from Pydantic schema if needed
