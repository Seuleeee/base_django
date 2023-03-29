import traceback
from typing import List

from django.core.mail import EmailMessage


class Emailservice:
    def send(
        self,
        *,
        subject: str = 'Hello!',
        body: str = 'world',
        to: List[str] = None,
    ):
        email = EmailMessage(
            subject=subject,
            body=body,
            to=to,
        )
        is_send: bool = email.send()

        if not is_send:
            print(traceback.format_exc())
