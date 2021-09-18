from .base import *

# Develop Debug Setup
DEBUG = True

ROOT_URLCONF = 'conf.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'

INSTALLED_APPS += [
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
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# AUTH USER MODEL
AUTH_USER_MODEL = "core.Account"
