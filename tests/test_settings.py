__author__ = 'naveenkumar'

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "mdc_logging",
]
MIDDLEWARE_CLASSES = (
    "mdc_logging.middleware.MDCMiddleware",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'mdc_formatter',
        },
    },
    'loggers': {
        'test_logger': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    'formatters': {
        'mdc_formatter': {
            '()': 'mdc_logging.formatter.MDCFormatter'
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

from django.conf.urls import url
from tests import header_view

ROOT_URLCONF = "tests.test_settings"

urlpatterns = [
    url(r'^header_test', header_view),
]

HEADERS_TO_LOG = ["new_header"]
