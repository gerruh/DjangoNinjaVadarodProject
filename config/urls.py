from django.contrib import admin
from django.urls import path
from rest_api.router import api as api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_router.urls),
]
