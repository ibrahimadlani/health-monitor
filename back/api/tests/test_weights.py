"""
Tests for the weight module.
"""

import pytest
from django.urls import reverse
from api.models import (
    NeckMeasurement,
    WaistMeasurement,
    ChestMeasurement,
    WeightMeasurement,
    BeltMeasurement,
    ThighMeasurement,
    WeightRecord,
    LovehandleMeasurement,
    CalfMeasurement,
    ArmMeasurement,
    ForearmMeasurement,
    ShoulderMeasurement,
)


@pytest.mark.django_db
def test_create_neck_measurement(api_client, create_user, get_token):
    """
    Check if a neck measurement can be created.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Payload for neck measurement creation
    payload = {
        "size": 40.0,
        "note": "Test neck measurement",
    }

    # Post to create neck measurement
    response = api_client.post(reverse("neck-measurement-create"), payload)

    # Assertions
    assert response.status_code == 201
    assert NeckMeasurement.objects.filter(user=user).exists()
    neck_measurement = NeckMeasurement.objects.get(user=user)
    assert neck_measurement.size == 40.0
    assert neck_measurement.note == "Test neck measurement"


@pytest.mark.django_db
def test_create_waist_measurement(api_client, create_user, get_token):
    """
    Check if a waist measurement can be created.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Payload for waist measurement creation
    payload = {
        "size": 85.0,
        "note": "Test waist measurement",
    }

    # Post to create waist measurement
    response = api_client.post(reverse("waist-measurement-create"), payload)

    # Assertions
    assert response.status_code == 201
    assert WaistMeasurement.objects.filter(user=user).exists()
    waist_measurement = WaistMeasurement.objects.get(user=user)
    assert waist_measurement.size == 85.0
    assert waist_measurement.note == "Test waist measurement"


@pytest.mark.django_db
def test_create_weight_measurement(api_client, create_user, get_token):
    """
    Check if a weight measurement can be created.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Payload for weight measurement creation
    payload = {
        "weight": 72.5,
        "note": "Test weight measurement",
    }

    # Post to create weight measurement
    response = api_client.post(reverse("weight-measurements-create"), payload)

    # Assertions
    assert response.status_code == 201
    assert WeightRecord.objects.filter(user=user).exists()
    weight_measurement = WeightRecord.objects.get(user=user)
    assert weight_measurement.weight == 72.5
    assert weight_measurement.note == "Test weight measurement"


@pytest.mark.django_db
def test_create_chest_measurement(api_client, create_user, get_token):
    """
    Checks if a chest measurement can be created.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Payload for chest measurement creation
    payload = {
        "size": 100.0,
        "note": "Test chest measurement",
    }

    # Post to create chest measurement
    response = api_client.post(reverse("chest-measurement-create"), payload)

    # Assertions
    assert response.status_code == 201
    assert ChestMeasurement.objects.filter(user=user).exists()
    chest_measurement = ChestMeasurement.objects.get(user=user)
    assert chest_measurement.size == 100.0
    assert chest_measurement.note == "Test chest measurement"


@pytest.mark.django_db
def test_create_belt_measurement(api_client, create_user, get_token):
    """
    Checks if a belt measurement can be created.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Payload for belt measurement creation
    payload = {
        "size": 90.0,
        "note": "Test belt measurement",
    }

    # Post to create belt measurement
    response = api_client.post(reverse("belt-measurement-create"), payload)

    # Assertions
    assert response.status_code == 201
    assert BeltMeasurement.objects.filter(user=user).exists()
    belt_measurement = BeltMeasurement.objects.get(user=user)
    assert belt_measurement.size == 90.0
    assert belt_measurement.note == "Test belt measurement"


@pytest.mark.django_db
def test_create_thigh_measurement(api_client, create_user, get_token):
    """
    Checks if a thigh measurement can be created.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Payload for thigh measurement creation
    payload = {"size": 60.0, "note": "Test thigh measurement"}

    # Post to create thigh measurement
    response = api_client.post(reverse("thigh-measurement-create"), payload)

    # Assertions
    assert response.status_code == 201
    assert ThighMeasurement.objects.filter(user=user).exists()
    thigh_measurement = ThighMeasurement.objects.get(user=user)
    assert thigh_measurement.size == 60.0
    assert thigh_measurement.note == "Test thigh measurement"


@pytest.mark.django_db
def test_list_neck_measurements(api_client, create_user, get_token):
    """
    Checks if neck measurements can be listed.
    """
    # Create a user and authenticate
    user = create_user()
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')

    # Create a neck measurement
    NeckMeasurement.objects.create(user=user, size=40.0)

    # Get neck measurements
    response = api_client.get(reverse("neck-measurement-list"))

    # Assertions
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["size"] == 40.0


@pytest.mark.django_db
def test_user_get_name(create_user):
    """
    Check if the user's full name is correct.
    """
    # Create a user and authenticate
    user = create_user(first_name="Test", last_name="User")

    # Assertions
    assert user.get_full_name() == "Test User"


@pytest.mark.django_db
def test_user_get_short_name(create_user):
    """
    Check if the user's short name is correct.
    """
    # Create a user and authenticate
    user = create_user(first_name="Test", last_name="User")

    # Assertions
    assert user.get_short_name() == "Test"


@pytest.mark.django_db
def test_user_has_perm(create_user):
    """
    Check if a user has a permission.
    """
    # Create a user and authenticate
    user = create_user(is_staff=True)

    # Assertions
    assert user.has_perm("test_perm") == True


@pytest.mark.django_db
def test_user_has_module_perms(create_user):
    """
    Check if a user has permission to view a module.
    """
    # Create a user and authenticate
    user = create_user(is_staff=True)

    # Assertions
    assert user.has_module_perms("test_app") == True


@pytest.mark.django_db
def test_weight_record_str(create_user):
    """
    Check if the string representation of a weight record is correct.
    """
    # Create a user and authenticate
    user = create_user()
    weight_record = WeightRecord.objects.create(user=user, weight=70.0)

    # Assertions
    assert str(weight_record) == f"{user} weighted 70.0kg on {weight_record.date}"


@pytest.mark.django_db
def test_neck_measurement_str(create_user):
    """
    Check if the string representation of a neck measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    neck_measurement = NeckMeasurement.objects.create(user=user, size=40.0)

    # Assertions
    assert str(neck_measurement) == f"{user} measured 40.0cm on {neck_measurement.date}"


@pytest.mark.django_db
def test_waist_measurement_str(create_user):
    """
    Check if the string representation of a waist measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    waist_measurement = WaistMeasurement.objects.create(user=user, size=85.0)

    # Assertions
    assert (
        str(waist_measurement) == f"{user} measured 85.0cm on {waist_measurement.date}"
    )


@pytest.mark.django_db
def test_chest_measurement_str(create_user):
    """
    Check if the string representation of a chest measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    chest_measurement = ChestMeasurement.objects.create(user=user, size=100.0)

    # Assertions
    assert (
        str(chest_measurement) == f"{user} measured 100.0cm on {chest_measurement.date}"
    )


@pytest.mark.django_db
def test_belt_measurement_str(create_user):
    """
    Check if the string representation of a belt measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    belt_measurement = BeltMeasurement.objects.create(user=user, size=90.0)

    # Assertions
    assert str(belt_measurement) == f"{user} measured 90.0cm on {belt_measurement.date}"


@pytest.mark.django_db
def test_thigh_measurement_str(create_user):
    """
    Check if the string representation of a thigh measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    thigh_measurement = ThighMeasurement.objects.create(user=user, size=60.0)

    # Assertions
    assert (
        str(thigh_measurement) == f"{user} measured 60.0cm on {thigh_measurement.date}"
    )


@pytest.mark.django_db
def test_lovehandle_measurement_str(create_user):
    """
    Check if the string representation of a lovehandle measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    lovehandle_measurement = LovehandleMeasurement.objects.create(user=user, size=70.0)

    # Assertions
    assert (
        str(lovehandle_measurement)
        == f"{user} measured 70.0cm on {lovehandle_measurement.date}"
    )


@pytest.mark.django_db
def test_calf_measurement_str(create_user):
    """
    Check if the string representation of a calf measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    calf_measurement = CalfMeasurement.objects.create(user=user, size=30.0)

    # Assertions
    assert str(calf_measurement) == f"{user} measured 30.0cm on {calf_measurement.date}"


@pytest.mark.django_db
def test_arm_measurement_str(create_user):
    """
    Check if the string representation of an arm measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    arm_measurement = ArmMeasurement.objects.create(user=user, size=30.0)

    # Assertions
    assert str(arm_measurement) == f"{user} measured 30.0cm on {arm_measurement.date}"


@pytest.mark.django_db
def test_forearm_measurement_str(create_user):
    """
    Check if the string representation of a forearm measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    forearm_measurement = ForearmMeasurement.objects.create(user=user, size=30.0)

    # Assertions
    assert (
        str(forearm_measurement)
        == f"{user} measured 30.0cm on {forearm_measurement.date}"
    )


@pytest.mark.django_db
def test_shoulder_measurement_str(create_user):
    """
    Check if the string representation of a shoulder measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    shoulder_measurement = ShoulderMeasurement.objects.create(user=user, size=30.0)

    # Assertions
    assert (
        str(shoulder_measurement)
        == f"{user} measured 30.0cm on {shoulder_measurement.date}"
    )


@pytest.mark.django_db
def test_weight_measurement_str(create_user):
    """
    Check if the string representation of a weight measurement is correct.
    """
    # Create a user and authenticate
    user = create_user()
    weight_measurement = WeightMeasurement.objects.create(user=user, weight=70.0)

    # Assertions
    assert (
        str(weight_measurement)
        == f"{user} weighted 70.0kg on {weight_measurement.date}"
    )
