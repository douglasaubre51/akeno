from django.urls import path,include
from django.contrib.auth import views as auth_views

# from dashboard import views

urlpatterns = [
        # login view
        path('',auth_views.LoginView.as_view()),

        # dashboard
        # path('dashboard',views.get_dashboard)
        ]
