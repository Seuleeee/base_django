from __future__ import annotations

from django.db import models

from api.constants.types import FileTypesEnum
from api.models.base import (
    BaseModel,
    TimestampedModel,
    TimestampedUserModel,
)


def get_upload_to(instance: SampleFileModel, file_name: str):
    """
    File Upload 시 저장 될 경로를 지정 하는 메소드
    settings.py (base.py)에서 설정한 MEDIA_ROOT 하위에
    return 되는 경로와 동일하게 파일 저장

    Client에서 받아온 type에 따라 저장 경로를 분기 할 수 있으며, 아래 소스코드 커스텀하여 사용
    예를 들어, Client에서 받아온 type 에 따라 validation check를 할 수도 있고
    file_path 커스텀 가능
    """
    if instance.type in FileTypesEnum.get_all_values():
        return f"{instance.type}/{file_name}"
    else:
        raise ValueError("Invalid File Type!!!")



class SampleFileModel(BaseModel):
    file = models.CharField(max_length=256, null=False)
    file_path = models.FileField(upload_to=get_upload_to, blank=False, null=False, default="")
    extension = models.CharField(max_length=256, null=False)
    type = models.CharField(max_length=10, null=False)
