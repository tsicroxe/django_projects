from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^post_message$', views.post_message, name='post_message'),
    # url(r'^register$', views.register, name='register'),
    # url(r'^process$', views.process, name='process'),
    # url(r'^login$', views.login, name='login'),
]
