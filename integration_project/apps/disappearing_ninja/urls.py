from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninja/$', views.tmnt, name='tmnt'),
    url(r'^ninja/(?P<color>\w+)$', views.ninja, name='ninja'),
]
