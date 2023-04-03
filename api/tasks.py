import time
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


@shared_task
def test_periodic_job():
    print("Test Complete!!!")


@shared_task()
def test_task(a, b):
    time.sleep(180)
    print(a+b)
    return a + b
