"""
각종 View에 대한 Sample
"""
from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response

from api.services.samples.file import SampleFileService


class SampleFileView(APIView):
    def post(self, request: HttpRequest):
        SampleFileService().upload(request)
        return Response(data="Created!", status=201)
    