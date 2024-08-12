from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from shop import views
from rest_framework.routers import SimpleRouter
from rest_framework import permissions, views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', include('djoser.urls.jwt')),  # JWT token URLs
]




