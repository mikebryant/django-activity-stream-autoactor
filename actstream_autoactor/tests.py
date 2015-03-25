"""Tests for actstream_autoactor"""

from django.contrib.auth.models import User
from django.test import TestCase

from mock import Mock

from .middleware import SetActorMiddleware
from .utils import actor_context, get_actor


class CurrentActorTestCase(TestCase):
    """Testing the current actor."""

    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

    def test_context_manager(self):
        '''Test the context manager.'''

        self.assertEqual(get_actor(), None)

        with actor_context(self.user1):
            self.assertEqual(get_actor(), self.user1)

        self.assertEqual(get_actor(), None)

    def test_middleware(self):
        '''Test the middleware.'''

        context_manager = SetActorMiddleware()
        request = Mock()
        request.user = self.user2
        response = Mock()

        self.assertEqual(get_actor(), None)
        self.assertEqual(context_manager.process_request(request), None)
        self.assertEqual(get_actor(), self.user2)
        self.assertEqual(
            context_manager.process_response(request, response),
            response,
        )
        self.assertEqual(get_actor(), None)
