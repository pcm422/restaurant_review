from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECRET['DATABASE']['NAME'],
        'USER': SECRET['DATABASE']['USER'],
        'PASSWORD': SECRET['DATABASE']['PASSWORD'],
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATIC_URL = '/static/'
STATIC_DIR = BASE_DIR / 'static'

STATIC_ROOT = BASE_DIR / '.static_root'


# Media
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'