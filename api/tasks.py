from typing import List

from celery import shared_task

from api.services.email import Emailservice


@shared_task
def send_email_task(subject: str, body: str, to: List[str]):
    return Emailservice().send(
        subject=subject,
        body=body,
        to=to
    )
