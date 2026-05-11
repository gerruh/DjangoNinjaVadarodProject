from django.contrib import admin
from django.urls import path
from django_ninja_project.rest_api.router import api as api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_router.urls),
]
