import json

from django.http import HttpRequest
from django.http import JsonResponse
from rest_framework import (
    views,
)
from rest_framework.response import Response

from celery.result import AsyncResult

from api.services.board import BoardService
from api.tasks import send_email_task, test_task


class Board(views.APIView):

    def get(self, request: HttpRequest, pk: int) -> Response:
        bs = BoardService()
        result = bs.get(pk)
        return Response(result)


class EmailAPI(views.APIView):
    def post(self, request):
        data = request.data

        task = send_email_task.delay(
            subject=data.get('subject'),
            body=data.get('body'),
            to=data.get('to')
        )
        return Response(
            {
                "task_id": task.id,
            },
            status=202,
        )


def get_status(request, task_id: str) -> JsonResponse:
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }

    return JsonResponse(result, status=200)

