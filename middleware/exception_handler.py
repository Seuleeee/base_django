import logging
import traceback
from datetime import datetime

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


logger = logging.getLogger('prod')

class ExceptionHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if not settings.DEBUG:
            if exception:
                now = datetime.now()
                api = request.build_absolute_uri()
                error = repr(exception)
                error_detail = traceback.format_exc()
                message = f'''\n\n
                API  : {api} \n
                Time : {now} \n
                Error: {error} \n
                Detail\n
                {error_detail} 
                '''
                logger.error(traceback.format_exc())
                send_mail(
                    subject=error,
                    message=message,
                    from_email=settings.EMAIL_HOST,
                    recipient_list=[settings.RECEIVE_ERROR_LOG_EMAIL],
                    fail_silently=False,
                )
                return HttpResponse(exception, status=500)
        return HttpResponse('Error', status=500)
