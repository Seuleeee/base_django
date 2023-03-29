from django.http import HttpRequest
from rest_framework import (
    views,
)
from rest_framework.response import Response


from api.tasks import send_email_task


class Board(views.APIView):

    def get(self, request: HttpRequest):
        return Response('인증 완료!!!!')


class EmailAPI(views.APIView):
    def post(self, request):
        data = request.data

        send_email_task.delay(
            subject=data.get('subject'),
            body=data.get('body'),
            to=data.get('to')
        )
        return Response('완료!')
