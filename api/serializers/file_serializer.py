from __future__ import annotations

from rest_framework import serializers
from django.db.models.fields.files import FileField

from api.models.file import SampleFileModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleFileModel
        fields = ("file", "file_path", "extension", "type")
