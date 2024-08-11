from django.contrib import admin
from django.urls import path, include
from .views import calculation

urlpatterns = [
    path("",calculation),
]
