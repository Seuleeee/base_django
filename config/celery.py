import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.base", # TODO: 이부분에서 에러 발생한 것 확인
)
app = Celery("config")

app.config_from_object(
    "django.conf:settings",
    namespace="CELERY",
)

app.autodiscover_tasks()

app.conf.timezone = 'Asia/Seoul'

app.conf.beat_schedule = {
    "test-periodic-job": {
        "task": "api.tasks.test_periodic_job",
        "schedule": crontab(
            minute=52
        )
    }
}
