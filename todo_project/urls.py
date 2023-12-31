"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todo_app.views import CategoryViewSet, TodoViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BLOG_API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'todos', TodoViewSet)#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),

    path('', include(router.urls)),
]



# urlpatterns += statistics(settings. 
# MEDIA_URL, document_root = settings.MEDIA_ROOT)