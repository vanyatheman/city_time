"""
web URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('timeshift.urls')),
    path('admin/', admin.site.urls),
]
