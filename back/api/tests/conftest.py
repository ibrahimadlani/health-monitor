"""
Fixtures for the tests
"""

import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def api_client():
    """Fixture for the API client"""
    return APIClient()


@pytest.fixture
def create_user():
    """Fixture to create a user"""

    def _create_user(
        email="testuser@example.com", password="password123", **extra_fields
    ):
        user = User.objects.create_user(email=email, password=password, **extra_fields)
        return user

    return _create_user


@pytest.fixture
def get_token():
    """Fixture to get a valid JWT token for a user"""

    def _get_token(user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    return _get_token
