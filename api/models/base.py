import re

from django.db import models


class BaseModel(models.Model):
    """
    기본 Django Model
    1. primary_key 를 AutoIncrement로 지정
    2. 상속 받은 Model의 Class Name을 snake case 로 변환하여, db_table로 지정
        - class name 만 뒤에 붙은 Model은 무시
    """
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

    def __init_subclass__(cls, **kwargs):
        cls.Meta.db_table = cls._set_table_name(cls.__name__)

    @staticmethod
    def _set_table_name(raw_name: str) -> str:
        class_name: str = re.sub(re.compile(r'Model$', re.IGNORECASE), '', raw_name).strip().replace(' ', '_')
        return re.sub(r"(?<!^)(?=[A-Z])", '_', class_name).lower()


class TimestampedModel(models.Model):
    """ DB Column으로 자주 사용되는 TimeStamp """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimestampedUserModel(TimestampedModel):
    """ TimeStamp에 user 정보 필요시 추가 """

    created_by = models.CharField(max_length=20)
    updated_by = models.CharField(max_length=20)

    class Meta:
        abstract = True
