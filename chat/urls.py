from django.urls import path

from . import views


urlpatterns = [
        path('<str:worker_id>/<str:room_guid>/',views.get_chat_page),

]
