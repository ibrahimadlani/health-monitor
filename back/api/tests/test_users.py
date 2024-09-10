"""
Users model tests
"""

import os
import django
import pytest
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    """
    Checks if a user is created successfully.
    """

    user = User.objects.create_user(
        email="testuser@example.com", username="testuser", password="testpass123"
    )
    assert user.email == "testuser@example.com"
    assert user.username == "testuser"
    assert user.check_password("testpass123") is True
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False


@pytest.mark.django_db
def test_create_superuser():
    """
    Checks if a superuser is created successfully.
    """

    superuser = User.objects.create_superuser(
        email="admin@example.com", username="adminuser", password="adminpass123"
    )
    assert superuser.email == "admin@example.com"
    assert superuser.username == "adminuser"
    assert superuser.check_password("adminpass123") is True
    assert superuser.is_active is True
    assert superuser.is_staff is True
    assert superuser.is_superuser is True


@pytest.mark.django_db
def test_create_staffuser():
    """
    Checks if a staff user is created successfully.
    """
    staffuser = User.objects.create_staffuser(
        email="staff@example.com", username="staffuser", password="staffpass123"
    )
    assert staffuser.email == "staff@example.com"
    assert staffuser.username == "staffuser"
    assert staffuser.check_password("staffpass123") is True
    assert staffuser.is_active is True
    assert staffuser.is_staff is True
    assert staffuser.is_superuser is False


@pytest.mark.django_db
def test_create_user_without_email():
    """
    Checks if an error is raised when creating a user without an email.
    """

    with pytest.raises(ValueError, match="The Email field must be set"):
        User.objects.create_user(
            email=None, username="noemailuser", password="nopass123"
        )


@pytest.mark.django_db
def test_create_user_with_duplicate_email():
    """
    Checks if an error is raised when creating a user with a duplicate email.
    """

    User.objects.create_user(
        email="duplicate@example.com", username="user1", password="testpass123"
    )
    with pytest.raises(IntegrityError):
        User.objects.create_user(
            email="duplicate@example.com", username="user2", password="testpass123"
        )


@pytest.mark.django_db
def test_user_str():
    """
    Checks if the user model returns the email as the string representation.
    """

    user = User.objects.create_user(
        email="struser@example.com", username="struser", password="strpass123"
    )
    assert str(user) == "struser@example.com"


@pytest.mark.django_db
def test_get_full_name():
    """
    Checks if the user model returns the full name.
    """
    user = User.objects.create_user(
        email="fullname@example.com",
        username="fullnameuser",
        first_name="John",
        last_name="Doe",
        password="testpass123",
    )
    assert user.get_full_name() == "John Doe"


@pytest.mark.django_db
def test_get_short_name():
    """
    Checks if the user model returns the short name.
    """
    user = User.objects.create_user(
        email="shortname@example.com",
        username="shortnameuser",
        first_name="Jane",
        password="testpass123",
    )
    assert user.get_short_name() == "Jane"
