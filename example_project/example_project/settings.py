'''Django settings for example_project project.'''
import os

from test_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.abspath(os.path.dirname(__file__)),'dbfile'),# Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'None'

WSGI_APPLICATION = 'example_project.wsgi.application'

try:
    from local_settings import *
except ImportError:
    pass

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
