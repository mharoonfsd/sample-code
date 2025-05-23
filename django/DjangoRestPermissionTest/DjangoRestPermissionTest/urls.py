"""DjangoRestPermissionTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from rest_framework import routers

from DjangoRestPermissionTest import views as drpt_views
from AnApp import views as aa_views

router = routers.DefaultRouter()
router.register(r'users', drpt_views.UserViewSet)
router.register(r'groups', drpt_views.GroupViewSet)
router.register(r'tests', drpt_views.TestModelViewSet)
router.register(r'other_tests', drpt_views.AnotherTestModelViewSet)
router.register(r'some_models', aa_views.SomeModelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
