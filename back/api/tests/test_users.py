"""
Test cases for the users app
"""

import pytest
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_user_creation(api_client):
    """
    Check if a user can be created
    """
    # Test user creation
    payload = {
        "email": "newuser@example.com",
        "username": "newuser",
        "password": "password123",
    }
    response = api_client.post("/api/users/create/", payload)
    assert response.status_code == 201
    assert "email" in response.data
    assert response.data["email"] == payload["email"]
    assert response.data["username"] == payload["username"]
    assert "password" not in response.data


@pytest.mark.django_db
def test_user_detail(api_client, create_user, get_token):
    """
    Check if a user can be retrieved
    """
    # Create user and get token
    user = create_user(email="testuser@example.com", username="testuser")
    token = get_token(user)

    # Test user detail view
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    response = api_client.get(f"/api/users/{user.id}/")

    assert response.status_code == 200
    assert response.data["email"] == "testuser@example.com"


@pytest.mark.django_db
def test_user_update(api_client, create_user, get_token):
    """
    Check if a user can be updated
    """
    # Create user and get token
    user = create_user(email="testuser@example.com", username="testuser")
    token = get_token(user)

    # Test user update
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    update_payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "first_name": "Updated",
        "last_name": "User",
    }
    response = api_client.put(f"/api/users/{user.id}/update/", update_payload)
    assert response.status_code == 200
    assert response.data["first_name"] == "Updated"
    assert response.data["last_name"] == "User"


@pytest.mark.django_db
def test_user_delete(api_client, create_user, get_token):
    """
    Check if a user can be deleted
    """
    # Create user and get token
    user = create_user(email="testuser@example.com", username="testuser")
    token = get_token(user)

    # Test user deletion
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    response = api_client.delete(f"/api/users/{user.id}/delete/")
    assert response.status_code == 204
