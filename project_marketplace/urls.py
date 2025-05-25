from django.urls import path

from . import views


urlpatterns = [
        path('',views.get_project_marketplace_page,name='project_marketplace')
        ]
