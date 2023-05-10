"""
각종 View에 대한 Sample
"""
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response


class SampleFileView(APIView):
    def post(self, request: HttpRequest):
        return Response("")