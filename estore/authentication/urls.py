from django.urls import include, path

from .views import RegisterUserView, UserListView

urlpatterns = [
    path("register/", RegisterUserView.as_view()),
    path("list/", UserListView.as_view()),
]
