from django.urls import re_path

from .consumers import DashboardConsumer


websocket_urlpatterns = [
        re_path(
            r'(?P<room_guid>[\w-]+)/$',
            DashboardConsumer.as_asgi()
            )
        ]
