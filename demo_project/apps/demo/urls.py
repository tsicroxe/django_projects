from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # url(r'^new$', views.new, name='new'),
    # url(r'^create$', views.create, name='create'),
    # url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    # url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    # url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    # url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),

]
