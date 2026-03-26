from django.urls import path

from . import views

urlpatterns = [

        path('<int:id>/',views.get_user_profile_page)

        ]
