"""
Django settings for minicall project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import raven
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r&fokr-eqimpu)a17i#vm-8yket30#(my(%o&uphf%02uks=oy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'colasIN',
    'discador',
    'comunica7',
    'app',
    'cdr',
    'callcenter',
    'speech',
    'import_export',
    'rest_framework',
    'ws4redis',
    'django_admin_listfilter_dropdown',
    'raven.contrib.django.raven_compat',
    
]





# WSGI_APPLICATION = 'minicall.wsgi.application'


WSGI_APPLICATION = 'ws4redis.django_runserver.application'

WEBSOCKET_URL = '/ws/'

WS4REDIS_EXPIRE = 3600

WS4REDIS_HEARTBEAT = '--heartbeat--'

WS4REDIS_PREFIX = 'demo'


SESSION_ENGINE = 'redis_sessions.session' # for djcelery

SESSION_REDIS_PREFIX = 'session'


RAVEN_CONFIG = {
    'dsn': 'https://8ce4ee7463a7401d96f3fad48c63b355@sentry.io/1259515',

    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




ROOT_URLCONF = 'minicall.urls'

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
                'ws4redis.context_processors.default',
            ],
        },
    },
]



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.datos'),
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql', 
    #     'NAME': 'comunica7',
    #     'USER': 'root',
    #     'PASSWORD': 'app01c7c0m2019',
    #     'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
    #     'PORT': '3306',
    # },
    # 'cdr': {
    #     'ENGINE': 'django.db.backends.mysql', 
    #     'NAME': 'cdr',
    #     'USER': 'root',
    #     'PASSWORD': 'd4t4B4$3*',
    #     'HOST': 'xiencias.com',   # Or an IP Address that your DB is hosted on
    #     'PORT': '3306',
    # },
    # 'discador': {
    #   'ENGINE': 'django.db.backends.sqlite3',
    #   'NAME': os.path.join(BASE_DIR, 'db.datos'),
    # },

    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.datos'),
    },
    'discador': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.datos'),
    }

}

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
os.path.join(BASE_DIR, "frontend"))


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


DATABASE_ROUTERS = ['cdr.router.CdrRouter',]