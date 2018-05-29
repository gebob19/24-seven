"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .user.views import UserViewSet
from .routes.basic import login, register
from .routes.friend_actions import send_friend_request, accept_friend_request

# MongoDB connection
from mongoengine import connect
connect('24-seven-test')

# set routes
router = routers.DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^register', register),

    url(r'^friend_actions/send_friend_request', send_friend_request),
    url(r'^friend_actions/accept_friend_request', accept_friend_request),
]

urlpatterns += router.urls
