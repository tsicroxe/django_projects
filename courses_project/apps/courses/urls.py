from django.conf.urls import url
from . import views
from views import index, create, destroy
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name='destroy'),
]
