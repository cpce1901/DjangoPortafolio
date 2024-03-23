from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "portaprod",  # Nombre DB
        "USER": "root",  # Nombre usuario
        "PASSWORD": "cpce1901",  # Password
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static/"
