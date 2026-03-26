from django.urls import path

from . import views


urlpatterns = [
        path('/sign-in',views.signIn),
        path('/sign-up',views.signUp),
        path('/sign-out',views.signOut)
]
