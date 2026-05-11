from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

urlpatterns = [
    path('admin/', admin.site.urls),
]

api = NinjaAPI()
