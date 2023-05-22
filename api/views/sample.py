"""
각종 View에 대한 Sample
"""
from django.http import HttpRequest

from rest_framework.views import (
    APIView,
)
from rest_framework.viewsets import (
    ModelViewSet,
)
from rest_framework.response import Response

from api.services.samples.file import SampleFileService
from api.models.sample import SampleModel
from api.serializers.sample_serializer import SampleSerializer


class SampleFileView(APIView):
    def post(self, request: HttpRequest):
        SampleFileService().upload(request)
        return Response(data="Created!", status=201)

    def get(self, request: HttpRequest, pk=None):
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
