from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views
# from dashboard import views

urlpatterns = [
        # login view
        path('',auth_views.LoginView.as_view()),

        #signup view
        path('signup',views.get_signup_page),
        # dashboard
        # path('dashboard',views.get_dashboard)
        ]
