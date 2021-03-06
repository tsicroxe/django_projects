"""integration_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^', include('apps.integration.urls', namespace='home')),
    url(r'^', include('apps.login_registration.urls', namespace='login_registration')),
    url(r'^random-word/', include('apps.random_word.urls', namespace='random_word')),
    url(r'^ninja-gold/', include('apps.ninja_gold.urls', namespace='ninja_gold')),
    url(r'^disappearing-ninja/', include('apps.disappearing_ninja.urls', namespace='disappearing_ninja')),
    url(r'^courses/', include('apps.courses.urls', namespace='courses')),
]
