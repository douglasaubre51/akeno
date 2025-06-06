"""
URL configuration for akeno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('__reload__/',include('django_browser_reload.urls')),

        path('admin/', admin.site.urls),

        # market place urls
        path('market_place/',include('market_place.urls')),

        # login
        path('',include('authentication.urls')),

        # dashboard
        path('dashboard/',include('dashboard.urls')),

        # user profile
        path('user_profile/',include('user_profile.urls')),

        # chat
        path('chat_room/',include('chat.urls')),

        # worker_dashboard
        path('worker_dashboard/',include('worker_dashboard.urls')),

        # project marketplace
        path('project_marketplace/',include('project_marketplace.urls'))
         
        ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
