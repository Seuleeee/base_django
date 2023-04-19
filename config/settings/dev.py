from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^http://localhost(:\d+)?$",
]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    "default": {
        "ENGINE": env('DEV_DB_ENGINE'),
        "NAME": env('DEV_DB_NAME'),
        "USER": env('DEV_DB_USER'),
        "PASSWORD": env('DEV_DB_PASSWORD'),
        "HOST": env('DEV_DB_HOST'),
        "PORT": env('DEV_DB_PORT'),
    }
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
    "APIS_SORTER": "alpha",
    "OPERATIONS_SORTER": "method",
    "TAGS_SORTER": "alpha",
}
