from django.conf.urls import url
from . import views
from views import index, create, destroy
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^courses_users$', views.courses_users, name='courses_users'),
    url(r'^create$', views.create, name='create'),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name='destroy'),
]
