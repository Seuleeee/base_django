from django.http import HttpRequest
from rest_framework import views, permissions
from rest_framework.response import Response

from api.services.board import BoardService


# Create your views here.
# Test, 참고해서 사용하세요.
class Board(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest):
        result = BoardService().create(request.data)
        return Response(result)
