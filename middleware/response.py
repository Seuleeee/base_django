from http.client import responses
import json

from dataclasses import dataclass
from typing import Dict

from django.http import JsonResponse
from rest_framework.status import is_success


class ResponseFormatter:
    def __init__(
        self,
        get_response
    ):
        self.get_response = get_response

    def __call__(self, request):
        """
        Custom Response Formatter
        1. Success인 경우 (200 ~ 299)
            - 그대로 response
        2. Error 발생한 경우
            - status_code 전달
            - error message
                - custom header
                - Reason-Phrase (HTTP/1.1 이후 표준)
        """
        response = self.get_response(request)
        status: int = response.status_code
        if is_success(status):
            """response.content는 utf-8로 decode해서 읽고, 이것을 dict로 만들어서 utf-8로 encodeing하고 response.content로 넣어줌"""

            return response
        else:
            message: str = response.message if hasattr(response, "message") else responses.get(status)
            response = JsonResponse(
                {
                    "error": message,
                },
                status=status,
            )
            response["X-Error-Message"] = message # custom Header
            # response.reason_phrase = message # HTTP/1.1 이후 보편적인 응답 상태 헤더

            return response

    @staticmethod
    def process_exception(request, exception):
        """
        EndPoint 진입 이후의 Exception 만 적용 됨.
        """

        if exception:
            exception.detail = exception.detail if hasattr(exception, "detail") else exception

            if hasattr(exception, "status_code"):
                exception.status_code = exception.status_code
            elif hasattr(exception, "code"):
                exception.status_code = exception.code
            else:
                exception.status_code = 500

            result = ExceptionResponse(
                message=str(exception.detail),
                status_code=int(exception.status_code),
            )

        else:
            result = ExceptionResponse
        return result


@dataclass(frozen=True)
class ExceptionResponse:
    message: str = "exception이 존재하지 않는 에러 발생"
    status_code: int = 500
