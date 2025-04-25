from django.urls import path,include
from .custom_login import TwoWayLogin

from . import views
# from dashboard import views

urlpatterns = [
        # login view
        path('',TwoWayLogin.as_view()),

        #signup view
        path('signup',views.get_signup_page),

        #worker signup view
        path('worker-signup',views.get_worker_signup_page),

        # dashboard
        # path('dashboard',views.get_dashboard)
        ]
