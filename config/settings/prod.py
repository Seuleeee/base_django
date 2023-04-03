import dj_database_url

from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": env('PROD_DB_ENGINE'),
        "NAME": env('PROD_DB_NAME'),
        "USER": env('PROD_DB_USER'),
        "PASSWORD": env('PROD_DB_PASSWORD'),
        "HOST": env('PROD_DB_HOST'),
        "PORT": env('PROD_DB_PORT'),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"}
    }
}

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

db_from_env = dj_database_url.config(
    conn_max_age=500,
)

DATABASES['default'].update(db_from_env)
