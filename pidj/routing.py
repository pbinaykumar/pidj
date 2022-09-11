from django.urls import path
from . import consumers
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
websocket_urlpaterns = [
    path('ws', consumers.ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(websocket_urlpaterns))
    }
)