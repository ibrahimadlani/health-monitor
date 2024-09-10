"""
This file is used to define the urls of the core app.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView

urlpatterns = [
    # Auth
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # Users
    path("users/", CustomUserListCreateView.as_view(), name="user-list-create"),
    path(
        "users/<int:pk>/",
        CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-retrieve-update-destroy",
    ),
]
