'''Automatic configuration for actstream_autoactor.'''

from django_autoconfig.autoconfig import OrderingRelationship

SETTINGS = {
    'INSTALLED_APPS': [
        'django.contrib.auth',
        'actstream',
    ],

    'MIDDLEWARE_CLASSES': [
        'actstream_autoactor.middleware.SetActorMiddleware',
    ],

    'SOUTH_MIGRATION_MODULES': {
        'actstream_autoactor': 'actstream_autoactor.south_migrations',
    },
}

RELATIONSHIPS = [
    OrderingRelationship(
        'MIDDLEWARE_CLASSES',
        'actstream_autoactor.middleware.SetActorMiddleware',
        after=[
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ],
    ),
]
