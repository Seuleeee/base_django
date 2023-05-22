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
        fields = ("id", "file", "file_path", "extension", "type")


class SampleSerializer(serializers.ModelSerializer):
    column = serializers.CharField(help_text="테스트용")
    class Meta:
        model = SampleModel
        fields = ("id", "column",)
