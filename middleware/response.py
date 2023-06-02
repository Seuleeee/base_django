from __future__ import annotations
import logging
import sys
import traceback
from http.client import responses
from dataclasses import dataclass

from django.http import JsonResponse
from django.utils import timezone
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
        tb = traceback.format_exc()
        CustomLogging(request=request).log_exception(tb=tb)

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


class CustomLogging:
    def __init__(self, *, request):
        self.logger = logging.getLogger('base_django_dev')
        self.request = request
    def log_exception(self, *, tb):
        self.logger.exception(f'{self.get_log_prefix(self.request)}\nTraceback: {tb}')

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    def get_log_prefix(self, request):
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        view_name = request.resolver_match.view_name
        api_name = request.path
        ip_address = self.get_client_ip(request)

        formatted_string = \
            f"""
            [Error]
            1. API : {api_name}
            2. LoginUser : {user}
            3. DjangoView : {view_name}
            4. ClientIP : {ip_address}
            """

        return formatted_string


    def generate_readable_timestamp(self):
        now = timezone.localtime(timezone.now())
        timestamp = now.strftime('%Y-%m-%d-%H-%M-%S-%f')[:-3]  # 마지막 3자리는 밀리초를 의미하므로 제외

        return timestamp


@dataclass(frozen=True)
class ExceptionResponse:
    message: str = "exception이 존재하지 않는 에러 발생"
    status_code: int = 500
