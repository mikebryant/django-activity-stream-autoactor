'''actstream_autoactor middleware.'''

from .utils import get_actor, set_actor, AutoActorError


class SetActorMiddleware(object):
    '''
    Set the current actor to be the logged in user.
    '''

    def process_request(self, request):
        '''
        Set the current actor.
        '''
        try:
            request.actstream_actor_old_actor = get_actor()
        except AutoActorError:
            request.actstream_actor_old_actor = None
        if not request.user.is_anonymous():
            set_actor(request.user)

    def process_response(self, request, response):
        '''
        Unset the current actor.
        '''
        set_actor(request.actstream_actor_old_actor)
        return response
