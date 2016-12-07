from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^process$', views.process, name='process'),
    url(r'^reset$', views.reset, name='reset'),

]
