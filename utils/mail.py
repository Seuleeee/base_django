from abc import ABC, abstractmethod

from django.conf import settings
from django.core.mail import send_mail


class Mail(ABC):
    @abstractmethod
    def send(self, title: str, message: str):
        pass


class ErrorMail(Mail):
    def send(self, title: str, message: str):
        is_send: bool = send_mail(
            subject=title,
            message=message,
            from_email=settings.EMAIL_HOST,
            recipient_list=[settings.RECEIVE_ERROR_LOG_EMAIL],
        )
        print(is_send)