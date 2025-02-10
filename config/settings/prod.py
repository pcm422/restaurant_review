from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://pcm0422.pythonanywhere.com/']

STATIC_URL = '/static/'
STATIC_DIR = BASE_DIR / 'static'

STATIC_ROOT = BASE_DIR / '.static_root'


# Media
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'