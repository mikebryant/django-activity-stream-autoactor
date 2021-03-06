DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
INSTALLED_APPS = ['actstream_autoactor']
ROOT_URLCONF = 'django_autoconfig.autourlconf'

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
