from django.http import HttpRequest
from rest_framework import (
    views,
    permissions,
)
from rest_framework.response import Response


from api.services.board import BoardService


class Board(views.APIView):

    def get(self, request: HttpRequest):
        return Response('인증 완료!!!!')
