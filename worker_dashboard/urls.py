from django.urls import path

from . import views


urlpatterns = [
        path(
            '',
            views.get_worker_dashboard_page
            )
        ]
