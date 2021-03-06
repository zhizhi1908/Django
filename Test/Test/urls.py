"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from testapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.acc_login, name='acc_login'),
    url(r'^article/(\d{4})/(\d{2})/(\d{2})/$', views.article),
    url(r'^index/$', views.index),
    url(r'^host/$', views.host, name='host'),
    url(r'^$', views.bootstrap),
    url(r'^asset/$', views.asset, name='asset'),
    url(r'^audit/$', views.audit, name='audit'),
    url(r'^logout/$', views.acc_logout),
    ]
