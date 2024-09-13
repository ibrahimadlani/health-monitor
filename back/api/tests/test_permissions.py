"""
Test the permissions of the api app
"""

import pytest
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from api.models import WeightMeasurement
from api.permissions import IsOwner, IsAdminOrOwner

User = get_user_model()


@pytest.fixture
def create_users():
    """Fixture to create test users (regular and admin)"""

    def _create_users():
        owner = User.objects.create_user(
            email="owner@example.com", password="password", username="owner"
        )
        non_owner = User.objects.create_user(
            email="nonowner@example.com", password="password", username="nonowner"
        )
        admin = User.objects.create_user(
            email="admin@example.com",
            password="password",
            username="admin",
            is_staff=True,
        )
        return owner, non_owner, admin

    return _create_users


@pytest.fixture
def create_weight_record(create_users):
    """Fixture to create a weight record associated with the owner"""
    owner, non_owner, admin = create_users()
    weight_record = WeightMeasurement.objects.create(user=owner, weight=70.0)
    return weight_record, owner, non_owner, admin


@pytest.mark.django_db
def test_is_owner_permission(create_weight_record):
    """
    Check if the IsOwner permission works as expected
    """
    weight_record, owner, non_owner, _ = create_weight_record
    factory = APIRequestFactory()
    view = None  # You can mock a view if needed

    # Owner request
    owner_request = factory.get("/weights/")
    owner_request.user = owner

    # Non-owner request
    non_owner_request = factory.get("/weights/")
    non_owner_request.user = non_owner

    # Test owner has permission
    permission = IsOwner()
    assert permission.has_object_permission(owner_request, view, weight_record) == True

    # Test non-owner does not have permission
    assert (
        permission.has_object_permission(non_owner_request, view, weight_record)
        == False
    )


@pytest.mark.django_db
def test_is_admin_or_owner_permission(create_weight_record):
    """
    Check if the IsAdminOrOwner permission works as expected
    """
    weight_record, owner, non_owner, admin = create_weight_record
    factory = APIRequestFactory()
    view = None  # You can mock a view if needed

    # Owner request
    owner_request = factory.get("/weights/")
    owner_request.user = owner

    # Non-owner request
    non_owner_request = factory.get("/weights/")
    non_owner_request.user = non_owner

    # Admin request
    admin_request = factory.get("/weights/")
    admin_request.user = admin

    # Test owner has permission
    permission = IsAdminOrOwner()

    # Test non-owner does not have permission
    assert (
        permission.has_object_permission(non_owner_request, view, weight_record)
        == False
    )

    # Test admin has permission
    assert permission.has_object_permission(admin_request, view, weight_record) == True
