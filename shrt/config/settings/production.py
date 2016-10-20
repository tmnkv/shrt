from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    'sh.idaproject',
    '192.241.128.127',
    '127.0.0.1:8000'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': '',
        'PORT': '',
    }
}

ROOT_URLCONF = 'config.urls'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'