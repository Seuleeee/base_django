import logging
import traceback
from datetime import datetime

from django.http import HttpResponse
from django.conf import settings

from api.tasks import send_error_mail


logger = logging.getLogger('prod')

class ExceptionHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            if exception:
                now = datetime.now()
                api = request.build_absolute_uri()
                error = repr(exception)
                error_detail = traceback.format_exc()
                message = f'''\n\n API: {api} \n Time: {now} \n Error: {error} \n Detail\n{error_detail}'''
                logger.error(traceback.format_exc())
                send_error_mail.delay(error, message)
                return HttpResponse(exception, status=500)
        return HttpResponse('Error', status=500)
