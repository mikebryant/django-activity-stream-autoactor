'''actstream_autoactor middleware.'''

from django.contrib.contenttypes.models import ContentType

from .models import AnonymousActor
from .utils import clear_actor, set_actor


class SetActorMiddleware(object):
    '''
    Set the current actor to be the logged in user.
    '''

    def process_request(self, request):
        '''
        Set the current actor.
        '''
        if request.user.is_anonymous():
            set_actor(ContentType.objects.get_for_model(AnonymousActor, for_concrete_model=False))
        else:
            set_actor(request.user)

    def process_response(self, _request, response):
        '''
        Unset the current actor.
        '''
        clear_actor()
        return response
