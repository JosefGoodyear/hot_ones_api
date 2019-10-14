"""hot_ones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from api.views import EpisodeView, HotSauceView, SeasonView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('episodes', EpisodeView)
router.register('seasons', SeasonView)
router.register('hotsauces', HotSauceView)

router.get_api_root_view().cls.__name__ = "Hot Ones API"
router.get_api_root_view().cls.__doc__ = "An API for the youtube series Hot Ones"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('schema/', get_schema_view(
        title='Hot Ones API Documentation'),
        name = 'openapi-schema'),
    path('documentation/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger')
]
