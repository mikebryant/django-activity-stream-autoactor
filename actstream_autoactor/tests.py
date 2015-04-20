"""Tests for actstream_autoactor"""

from django.contrib.auth.models import User
from django.test import TestCase

from actstream import registry

from mock import Mock

from .middleware import SetActorMiddleware
from .utils import action_send, actor_context, get_actor, AutoActorError


class CurrentActorTestCase(TestCase):
    """Testing the current actor."""

    def setUp(self):
        registry.register(User)
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

    def test_context_manager(self):
        '''Test the context manager.'''

        self.assertRaises(AutoActorError, get_actor)

        with actor_context(self.user1):
            self.assertEqual(get_actor(), self.user1)

        self.assertRaises(AutoActorError, get_actor)

    def test_middleware(self):
        '''Test the middleware.'''

        context_manager = SetActorMiddleware()
        request = Mock()
        request.user = self.user2
        response = Mock()

        self.assertRaises(AutoActorError, get_actor)
        self.assertEqual(context_manager.process_request(request), None)
        self.assertEqual(get_actor(), self.user2)
        self.assertEqual(
            context_manager.process_response(request, response),
            response,
        )
        self.assertRaises(AutoActorError, get_actor)

    def test_action_send(self):
        '''Test the action_send method.'''

        with actor_context(self.user1):
            action_send(verb='did something')

        action = self.user1.actor_actions.all()[0]
        self.assertEqual(action.actor, self.user1)
