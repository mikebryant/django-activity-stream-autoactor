'''actstream_autoactor utilities.'''

from actstream import action

import contextlib
import threading

ACTOR_STORAGE = threading.local()
ACTOR_STORAGE.actor = None


def get_actor():
    '''Return the currently set actor.'''
    return ACTOR_STORAGE.actor


def set_actor(actor):
    '''Set the current actor.'''
    ACTOR_STORAGE.actor = actor


@contextlib.contextmanager
def actor_context(actor):
    '''Set the current actor as a context manager.'''
    old_actor = get_actor()
    set_actor(actor)
    yield
    set_actor(old_actor)


def action_send(*args, **kwargs):
    '''Send an action defaulting the actor to auto actor.'''
    actor = kwargs.pop('actor', None) or get_actor()
    return action.send(actor, *args, **kwargs)
