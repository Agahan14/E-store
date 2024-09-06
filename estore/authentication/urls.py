from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import ChangePasswordView, RegisterUserView, UserListView, UserLoginView

urlpatterns = [
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterUserView.as_view()),
    path("list/", UserListView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
]
