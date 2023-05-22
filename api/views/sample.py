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
