"""
각종 View에 대한 Sample
"""
import json

from django.http import (
    HttpRequest,
    JsonResponse,
)
from django.core import serializers
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import (
    APIView,
)
from rest_framework.viewsets import (
    ModelViewSet,
)
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from api.repos.sample import sample_repo
from api.services.samples.file import SampleFileService
from api.models.sample import SampleModel
from api.serializers.sample_serializer import SampleSerializer


class SampleFileView(APIView):
    def post(self, request: HttpRequest):
        SampleFileService().upload(request)
        return Response(data="Created!", status=201)

    def get(self, request: HttpRequest, pk: int=None):
        if pk is not None:
            result = SampleFileService().get(pk=pk)
        else:
            result = SampleFileService().get_multi()
        return Response(data=result, status=200)

    def put(self, request: HttpRequest, pk: int):
        result = SampleFileService().update(request=request, pk=pk)
        return Response(data=result, status=200)

    def delete(self, request: HttpRequest, pk: int):
        result = SampleFileService().delete(pk=pk)
        return Response(data=result, status=204)


class SampleModelViewSet(ModelViewSet):
    """
    Model ViewSet 상속으로 지정한 Model, Serializer를 활용해 RestfulAPI를 자동으로 생성
    1. Create : POST
    2. Read   : GET(Single, Multiple)
    3. Update : PUT, PATCH
    4. Delete : DELETE
    """
    queryset = SampleModel.objects.all()
    serializer_class = SampleSerializer


class SampleAPIView(APIView):
    """ CRUD시, Serializer를 활용하지 않고 ORM을 사용하는 예제 """
    @swagger_auto_schema(request_body=SampleSerializer, tags=["sample-apiview"])
    def post(self, request: HttpRequest):
        # TODO: 원하는 Data 형태로 가공 하여 사용하세요.
        data = request.data
        sample_repo.create(created_data=data)
        return Response("Success!", status=201)

    @swagger_auto_schema(tags=["sample-apiview"])
    def get(self, request: HttpRequest, pk: int=None):
        """
        ORM을 사용하여, 결과 값 Response 예제 입니다.
        단순 예시 이기에 Single, Multi Value 관계없이 Iterable한 객체로 반환 하고 있습니다.

        RestfulAPI의 URI Parameter로 pk 전달 유무에 따라 Single, Multi를 결정합니다.

        아래 TODO 참고하여, 적절하게 수정하여 사용하십시오.
        """
        if pk is not None:
            instance = sample_repo.get(pk=pk)
            # TODO: Single Instance 반환 방법 수정하여 사용하세요.
            serializer = SampleSerializer(instance)
            return Response(serializer.data)
        else:
            instance = sample_repo.get_multi()
            paginator = PageNumberPagination()
            paginated_queryset = paginator.paginate_queryset(instance, request)
            serializer = SampleSerializer(paginated_queryset, many=True)
            paginated_data = paginator.get_paginated_response(serializer.data)
            return paginated_data

    @swagger_auto_schema(request_body=SampleSerializer, tags=["sample-apiview"])
    def put(self, request: HttpRequest, pk: int):
        # TODO: 원하는 Data 형태로 가공 하여 사용하세요.
        data = request.data
        sample_repo.update(updated_data=data, pk=pk)
        return Response("Success!", status=200)

    @swagger_auto_schema(tags=["sample-apiview"])
    def delete(self, request: HttpRequest, pk: int):
        sample_repo.delete(pk=pk)
        return Response("Deleted!", status=204)
