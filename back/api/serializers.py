"""
API module serializers.
"""

from rest_framework import serializers
from api.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    This class is used to serialize the CustomUser model.
    """

    class Meta:
        """
        This class is used to define the fields that need to be serialized.
        """

        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "country_code",
            "city",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
