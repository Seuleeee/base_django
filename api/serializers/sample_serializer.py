from __future__ import annotations

from rest_framework import serializers
from django.db.models.fields.files import FileField

from api.models.sample import (
    SampleFileModel,
    SampleModel,
)

"""
Sample API 적용을 위한 Serializer 모음

1. File Upload
2. ModelViewSet
"""


class SampleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleFileModel
        fields = ("file", "file_path", "extension", "type")


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = ("id", "column",)
