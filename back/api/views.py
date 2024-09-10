"""
This file is used to define the views of the core app.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import CustomUser
from api.serializers import CustomUserSerializer


class CustomUserListCreateView(generics.ListCreateAPIView):
    """
    This class is used to define the views for listing and creating users.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class is used to define the views for retrieving, updating and deleting users.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
