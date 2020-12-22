from .wsgi import *
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing as routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
          re_path(r"^longpoll/$", LongPollConsumer.as_asgi()),
          re_path(r"^notifications/(?P<stream>\w+)/$", LongPollConsumer.as_asgi()),
          re_path(r"", get_asgi_application()),
])
        ]
            chat.routing.websocket_urlpatterns
        )
    ),
})
