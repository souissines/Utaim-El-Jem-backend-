"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.db import router
from django.template.defaulttags import url
from django.urls import path, include,re_path
from rest_framework import routers

from activity.views import ActivityViewSet
from api import views

from backend import settings

router = routers.DefaultRouter()
router.register('activities', ActivityViewSet)
router.register('boxes', views.BoxViewSet)
urlpatterns = [
    path('', include('public.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),

    path('api/auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
re_path(r'^', include(router.urls)),
    re_path(r'^', include('ActivityApp.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)