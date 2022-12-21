from celery import shared_task

from utils.mail import ErrorMail


@shared_task
def send_error_mail(title: str, message: str):
    return ErrorMail().send(title, message)
