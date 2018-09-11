"""
Django settings for khaja project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's0$n$+^sfk$1h7wl-tc3^q4mm72$p(^%!&y^b538sm2^8sdm&b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["khaja.com", 'localhost', '192.168.100.18','0.0.0.0',"khaja.herokuapp.com"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'products',
    'carts',
    'mathfilters',
    'wishlists',
    'orders',
    'addresses',
    'search',
    'company',
    'djcelery',
    'kombu.transport.django',
    'widget_tweaks',
    'delivery',
]

import djcelery
djcelery.setup_loader()
BROKER_URL = "django://"
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_IMPORTS = ("khaja.tasks",)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'khaja.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'khaja.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# #
'''DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'khaja',
       'USER': 'shital',
       'PASSWORD': 'luitel@dell.com',
       'HOST': 'localhost',
       'PORT': '5432',
	}
}'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd73r6tk635hhs0',
        'USER': 'izghiuqtdnftik',
        'PASSWORD': '1f914ec207fa48316b1408e31990c3add034c6953a6f3907d005304dfede547d',
        'HOST': 'ec2-54-247-100-44.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# media file (images file and all other stuff)
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGIN_URL = '/users/login/'
AUTH_USER_MODEL = 'users.User'

BASE_URL = 'http://khaja.herokuapp.com/'
ADMIN_EMAIL = 'noreply@khaja.com'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'luitelctal1@gmail.com'
EMAIL_HOST_PASSWORD = 'c0d3r5@luitel.87'
EMAIL_PORT = 587

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# AUTHENTICATION_BACKENDS = {
#     'django.contrib.auth.backends.RemoteUserBackend',
#     'django.contrib.auth.backends.ModelBackend',
# }
