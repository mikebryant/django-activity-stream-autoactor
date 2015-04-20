"""Models for actstream_autoactor."""

from django.contrib.auth.models import User

class UnknownActor(User):
    class Meta:
        proxy = True

class AnonymousActor(User):
    class Meta:
        proxy = True
