from django.urls import path
from .views import UserListAPI, UserDetailAPI

urlpatterns = [
    path("v1/users", UserListAPI.as_view(), name="user-list"),
    path("v1/users/<int:id>", UserDetailAPI.as_view(), name="user-detail"),
]
