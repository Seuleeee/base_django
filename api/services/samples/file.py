from __future__ import annotations
import traceback
from dataclasses import dataclass
from typing import (
    List,
    Any,
    Union,
)

from django.db import transaction
from django.http import QueryDict, HttpRequest

from api.serializers.sample_serializer import SampleFileSerializer
from utils.file import (
    get_file_extension,
    get_file_type,
)
from api.repos.sample import (
    sample_file_repo,
)


class SampleFileService:
    def upload(self, request: HttpRequest):
        """ Client 로 부터 전달 받은 request로 부터 File을 Upload """
        files = request.FILES.getlist(key='file', default=None)
        serializers = self._get_file_serializers(files=files)
        self._save(serializers=serializers)

    def update(self, request: HttpRequest, pk: int):
        instance = sample_file_repo.get(pk=pk)
        file = request.FILES.get(key='file', default=None)
        serializer = self._create_sample_file_serializer(file=file, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            print("Error!", traceback.format_exc())

    def _get_file_serializers(self, *, files: QueryDict) -> List[SampleFileSerializer]:
        """ 파일 개수(단, 복수) 와 관계 없이 Serializers 생성 """
        serializers = [
            self._create_sample_file_serializer(file=file)
            for file in files
        ]
        return serializers

    def _create_sample_file_serializer(self, *, file, instance=None) -> SampleFileSerializer:
        return SampleFileSerializer(instance, data=self._create_file_input_data(file=file))

    def _create_file_input_data(self, *, file):
        return FileInputData(
                file=file.name,
                file_path=file,
                extension=get_file_extension(file.name),
                type=get_file_type(file.name),
            ).__dict__

    @transaction.atomic
    def _save(self, *, serializers: List[SampleFileSerializer]):
        for serializer in serializers:
            if serializer.is_valid():
                serializer.save()
            else:
                print(traceback.format_exc())
                raise ValueError("파일 업로드 실패!")

    def delete(self, pk: int):
        instance = sample_file_repo.get(pk=pk)
        instance.delete()

    def get_multi(self):
        instance = sample_file_repo.get_multi()
        serializer = SampleFileSerializer(instance, many=True)
        return serializer.data

    def get(self, pk: int):
        data = sample_file_repo.get(pk=pk)
        serializer = SampleFileSerializer(data)
        return serializer.data


@dataclass
class FileInputData:
    file: str
    file_path: Union[str, Any]
    extension: str
    type: str
