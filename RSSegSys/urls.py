'''
Description: 
Author: M.H.
Date: 2024-01-26 14:28:25
LastEditTime: 2024-03-01 09:34:44
LastEditors: M.H.
Reference: 
'''
"""bookManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.views.generic.base import RedirectView

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.home),
    path('getstart/', views.getstart),
    path('userlur/', views.userLur),
    path('userupdate/', views.userupdate),
    path('userinfo/', views.userinfo),
    path('upload/', views.upload),
    path('record/', views.record),
    path('logout/', views.logout),
    path('favicon.ico', RedirectView.as_view(url='static/img/favicon.ico')),
    re_path(r'^api/', include('api.urls')),  # 将路由分发到api的urls
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
