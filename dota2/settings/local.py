from .base import *

DEBUG = True

SECRET_KEY = '3x@4#rx0fwt15gf-&@=0f3xzxrto_oz2r3=&zdc5mg(&)vhi-t'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dota2db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}