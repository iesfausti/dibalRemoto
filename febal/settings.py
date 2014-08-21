"""
21/8/2014 El proyecto ahora está en GITHUB, es público.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if socket.gethostname().startswith('casa-PC'):
	PROJECT_ROOT = "C:/Python/dibalRMS/"
	STATIC_URL = '/static/'
	ADMIN_MEDIA_PREFIX = '/static/admin/'
	
else:
	PROJECT_ROOT ="/home/febal/projects/febal/"
	STATIC_URL = '/static/'
	ADMIN_MEDIA_PREFIX = '/static/admin/'
	STATIC_ROOT = "/home/febal/projects/febal/public/static/"
	
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$cjs*%1$$ly+!8pv9d3+n+c1t6tzedn*$p%zk2btc6=o)+wud%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'

# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'febal',
    'informes',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'febal.urls'

WSGI_APPLICATION = 'febal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(PROJECT_ROOT, 'febal/febal/dibal.db'),
    #},
    
    'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '***',# Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '***',
            'PASSWORD': '***',
            'HOST': '***',                      # 
            'PORT': '',                      # Set to empty string for default.

    },

}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'es-ES'

SITE_ID = 1
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)




TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'informes/templates/'),


)

ADMIN_TOOLS_MENU = 'febal.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'febal.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'febal.dashboard.CustomAppIndexDashboard'
