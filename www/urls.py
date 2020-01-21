"""learndjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    # url(r'', include("risk_auth.urls", namespace='risk_auth')),
    # url(r'permissions/', include("permissions.urls", namespace="permissions")),
    # url(r'strategy/', include("strategy.urls", namespace="strategy")),
    url(r'menu/', include("menu.urls", namespace="menus")),
    # url(r'rule/', include("rule.urls", namespace="rule")),
    # url(r'config/', include("bk_config.urls", namespace="config")),
    # url(r'log_manage/', include("log_manage.urls", namespace="log_manage")),
]

# 用于线上时应移除此部分，动静分离


if not settings.DEBUG:
    from django.views.defaults import (page_not_found, server_error,
                                       permission_denied)

    urlpatterns += [
        url(r'404/', page_not_found),
        url(r'500/', server_error),
        url(r'403/', permission_denied),
    ]
