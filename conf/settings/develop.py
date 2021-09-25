from .base import *

# Develop Debug Setup
DEBUG = True

ROOT_URLCONF = 'conf.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'

INSTALLED_APPS += [
    'django_filters',
    'rest_framework',
    'coreapi',
    'drf_yasg',
    'mysite',
    'core',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'chinook.db',
    }
}

# Configuration
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

# Redoc Settings
REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}

# AUTH USER MODEL
AUTH_USER_MODEL = "core.AccountModel"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'sql': {
            '()': 'django_sqlformatter.SqlFormatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}
