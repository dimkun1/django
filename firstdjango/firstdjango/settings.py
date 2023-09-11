"""
Django settings for firstdjango project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-56eql7*l@gt$ow0)^ik&7&17jr29i$5f^i3n-f!2@ych%0&$jb'
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True
# server
DEBUG = False
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# ALLOWED_HOSTS = ['192.168.1.64', ]
ALLOWED_HOSTS = [
    '127.0.0.1',
    'testyyy.pythonanywhere.com',
]

INTERNAL_IPS = [
    '127.0.0.1',

]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', 'myapp1', 'myapp2', 'myapp3', 'myapp4', 'myapp5', 'myapp6', 'myapp7', 'myapp8', 'myapp9', 'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'firstdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'firstdjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {'default':
                 {'ENGINE': 'django.db.backends.mysql',
                  'NAME': 'testyyy$default',
                  'USER': 'testyyy',
                  'PASSWORD': os.getenv('MYSQL_PASSWORD'),
                  'HOST': 'testyyy.mysql.pythonanywhere-services.com',
                  'OPTIONS': {'init_command': "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",
                              'charset': 'utf8mb4',
                              },
                  }
             }
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

# MEDIA_DIR = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process} {thread} {message}',
            'style': '{',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
        'file1': {
            'class': 'logging.FileHandler',
            'filename': './log/django.log',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
        'file2': {
            'class': 'logging.FileHandler',
            'filename': './log/django_app1.log',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
        'file3': {
            'class': 'logging.FileHandler',
            'filename': './log/django_app2.log',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
        'file4': {
            'class': 'logging.FileHandler',
            'filename': './log/django_app3.log',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
        'file7': {
            'class': 'logging.FileHandler',
            'filename': './log/django_app7.log',
            'formatter': 'verbose',  # добавлен параметр formatter
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file1'],
            'level': 'INFO',
        },

        'myapp': {
            'handlers': ['console', 'file2'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp1': {
            'handlers': ['console', 'file3'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp2': {
            'handlers': ['console', 'file4'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp7': {
            'handlers': ['console', 'file7'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
