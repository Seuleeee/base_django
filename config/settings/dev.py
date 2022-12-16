from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    "default": {
        "ENGINE": env('DEV_DB_ENGINE'),
        "NAME": env('DEV_DB_NAME'),
        "USER": env('DEV_DB_USER'),
        "PASSWORD": env('DEV_DB_PASSWORD'),
        "HOST": env('DEV_DB_HOST'),
        "PORT": env('DEV_DB_PORT'),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"}
    }
}
