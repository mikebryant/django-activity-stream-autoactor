# django-activity-stream-autoactor

This addon package for [django-activity-stream](https://github.com/justquick/django-activity-stream) gives an easier way to utilise actions within library code, or model methods.

Instead of passing through a user/request object to everywhere that needs to record an action, using `utils.action_send` will use the current actor (defaulting to the logged in user).

Alternatively from a management command you can register a system user to be recorded as being responsible for any actions taken.

## Usage
```
# To send an action, use the normal parameters as for `action.send`, skipping the `actor`
actstream_autoactor.utils.action_send(verb='reached level 10')

# To set the current actor
with actstream_autoactor.utils.actor_context(User.objects.get(username='system')):
    action_send(verb='did something')
```

## Installation
If using [django-autoconfig](https://github.com/mikebryant/django-autoconfig), simply add `actstream_autoactor` to `INSTALLED_APPS`

Otherwise, add `actstream_autoactor.middleware.SetActorMiddleware` to `MIDDLEWARE_CLASSES` after authentication middleware
