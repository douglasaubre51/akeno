from django.urls import re_path
from channels.routing import URLRouter

from . import consumers
from dashboard.routing import websocket_urlpatterns as ws_urlpatterns


websocket_urlpatterns = [
        re_path(
            r"^chat_room/(?P<room_guid>[\w-]+)/$",
            consumers.CustomConsumer.as_asgi()
            ),
        re_path(
            'dashboard/',
            URLRouter(
                ws_urlpatterns
                )
            )
]
