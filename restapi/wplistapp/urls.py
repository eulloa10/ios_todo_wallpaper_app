"""wplistapp URL Configuration

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
from django.conf.urls  import *
from django.contrib import admin
from rest_framework import routers
from wplapp import views

#urlpatterns = [
#   path('admin/', admin.site.urls),
#]
router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'api/wplapp', views.FishViewSet)
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'marine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
