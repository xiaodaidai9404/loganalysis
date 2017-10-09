"""loganalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from loganalysis.view import index,country_loganalysis,country_get,http_code_get,http_code_loganalysis,test,slow_url_loganalysis,slow_url_get,slow_url_domain
from alert.view import alert_user,add_alert_user,del_alert_user,alert_rule,add_alert_rule

urlpatterns = [
    url(r'^$', index),
    url(r'^test/$',test),
    url(r'^loganalysis/country/$', country_loganalysis),
    url(r'^get/country/$', country_get),
    url(r'^loganalysis/httpcode/$',http_code_loganalysis),
    url(r'^get/httpcode/$',http_code_get),
    url(r'^loganalysis/slowurl/$',slow_url_loganalysis),
    url(r'^get/slowurl/$',slow_url_get),
    url(r'^get/domain/$',slow_url_domain),
    url(r'^alert/user/$',alert_user),
    url(r'^add/alert_user/$',add_alert_user),
    url(r'^del/alert_user/$',del_alert_user),
    url(r'^alert/rule/$',alert_rule),
    url(r'^add/alert_rule/$',add_alert_rule),
]
