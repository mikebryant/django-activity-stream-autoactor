'''Automatic configuration for actstream_autoactor.'''

from django_autoconfig.autoconfig import OrderingRelationship

SETTINGS = {
    'INSTALLED_APPS': [
        'django.contrib.auth',
    ],

    'MIDDLEWARE_CLASSES': [
        'actstream_autoactor.middleware.SetActorMiddleware',
    ],
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
