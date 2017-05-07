from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['.kusjesmachine.com']
WWW_HOST = "www.kusjesmachine.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'kusjesmachine'),
        'USER': os.getenv('DATABASE_USER', 'kusjesmachine'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'kusjesmachine'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}