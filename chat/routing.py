from django.urls import re_path

from . import consumers

websocket_urlpatterns = [

        re_path(r"^chat_room/(?P<room_guid>[\w-]+)/$",consumers.CustomConsumer.as_asgi())
]
