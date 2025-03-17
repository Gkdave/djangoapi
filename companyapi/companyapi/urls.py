"""
URL configuration for companyapi project.
  
"""
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index),
    path('api/dave/',include('api.urls')),
]
