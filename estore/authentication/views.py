from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (
    ChangePasswordSerializer,
    RegisterUserSerializer,
    UserLoginSerializer,
)


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data.get("email")  # agahan@gmail.com
        password = request.data.get("password")  # 12345678

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response({"error": "User not found!"}, status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
            raise AuthenticationFailed({"error": "Incorrect password!"})

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),  # 1 week
                "access": str(refresh.access_token),  # 5 minute
            }
        )


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        new_password = serializer.validated_data.get("new_password")
        user.set_password(new_password)
        user.save()

        return Response({"success": "Password changed successfully!"})
