'''actstream_autoactor middleware.'''

from .utils import get_actor, set_actor


class SetActorMiddleware(object):
    '''
    Set the current actor to be the logged in user.
    '''

    def process_request(self, request):
        '''
        Set the current actor.
        '''
        request.actstream_actor_old_actor = get_actor()
        if not request.user.is_anonymous():
            set_actor(request.user)

    def process_response(self, request, response):
        '''
        Unset the current actor.
        '''
        set_actor(request.actstream_actor_old_actor)
        return response
