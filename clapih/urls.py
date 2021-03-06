"""clapih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from UserApis.base.router import api_urlpatterns as api_v1
from UserApis.base.CLThreatsApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_v1)),
    # url(r'^api/v1/urlinfo/1/{[A-Za-z]}', views.UrlCheckView.as_view(), name='threat-list'),
    url(r'^api/v1/urlinfo/1/(?P<hostname>\w+)/(?P<original_path>\w+)/$', views.UrlCheckView.as_view(), name='threat-list'),
    url(r'^api/v1/urlinfo/1/(?P<hostname>\w+)/$', views.UrlCheckView.as_view(), name='threat-list'),
    url(r'^api/v1/urlinfo/1/(?P<hostname>[a-zA-Z0-9_.-/:?=#]*)/$', views.UrlCheckView.as_view(), name='threat-list'),

]
