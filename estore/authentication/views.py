from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
