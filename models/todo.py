from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

from .user import User  

class Todo(models.Model):
    sno = fields.IntField(pk=True)
    title = fields.CharField(max_length=20, unique=True)
    desc = fields.CharField(max_length=50, null=True)
    completed = fields.BooleanField(default=False)

    user = fields.ForeignKeyField(
        'models.User',
        related_name='todos',
        to_field='id',
        on_delete=fields.OnDelete.RESTRICT
    )

