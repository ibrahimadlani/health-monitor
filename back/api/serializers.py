"""
API module serializers.
"""

from rest_framework import serializers
from api.models import (
    CustomUser,
    ChestMeasurement,
    WaistMeasurement,
    NeckMeasurement,
    ThighMeasurement,
    BeltMeasurement,
    LovehandleMeasurement,
    CalfMeasurement,
    ArmMeasurement,
    ShoulderMeasurement,
    ForearmMeasurement,
    WeightRecord,
)


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user.
    """

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "country_code",
            "city",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Override the create method to handle password hashing.
        """
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            country_code=validated_data.get("country_code", ""),
            city=validated_data.get("city", ""),
        )
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving user details.
    """

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "country_code",
            "city",
        ]


class NeckDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving neck measurements.
    """

    class Meta:
        model = NeckMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class ChestDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving chest measurements.
    """

    class Meta:
        model = ChestMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class WaistDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving waist measurements.
    """

    class Meta:
        model = WaistMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class ThighDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving thigh measurements.
    """

    class Meta:
        model = ThighMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class WeightDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving weight records.
    """

    class Meta:
        model = WeightRecord
        fields = ["id", "date", "weight", "note", "user"]
        read_only_fields = ["user"]


class BeltDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving belt measurements.
    """

    class Meta:
        model = BeltMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class LovehandleDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving lovehandles measurements.
    """

    class Meta:
        model = LovehandleMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class CalfDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving calf measurements.
    """

    class Meta:
        model = CalfMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class ArmDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving arm measurements.
    """

    class Meta:
        model = ArmMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class ShoulderDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving shoulder measurements.
    """

    class Meta:
        model = ShoulderMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]


class ForearmDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving forearm measurements.
    """

    class Meta:
        model = ForearmMeasurement
        fields = ["id", "date", "size", "note", "user"]
        read_only_fields = ["user"]
