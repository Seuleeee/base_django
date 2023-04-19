from django.db import models

from api.models.base import (
    BaseModel,
    TimestampedModel,
    TimestampedUserModel,
)


class SampleBoard(BaseModel, TimestampedUserModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
