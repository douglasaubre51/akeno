from django.urls import path

from . import views

urlpatterns = [
        # market place
        path('',views.get_worker_market_place),

        # current time
        path('time/',views.get_current_time),

        path('message/<int:worker_id>/',views.init_message_room,name = 'init-message-room')
        ]
