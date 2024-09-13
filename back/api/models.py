"""
This file contains the models for the core app.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    This class is used to create user, superuser and staffuser.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        This method is used to create a user.
        """

        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        This method is used to create a superuser.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        """
        This method is used to create a staff user.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    This class is used to create a custom user model.
    """

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    country_code = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """
        String representation of the user.
        """
        return self.email

    def get_full_name(self):
        """
        Returns the full name of the user.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        Returns the short name of the user.
        """
        return self.first_name

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission.
        """
        return self.is_staff

    def has_module_perms(self, app_label):
        """
        Returns True if the user has permission to view the app 'app_label'.
        """
        return self.is_staff


class WeightRecord(models.Model):
    """
    This class is used to create a weight record model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the weight record.
        """
        return f"{self.user} weighted {self.weight}kg on {self.date}"


class NeckMeasurement(models.Model):
    """
    This class is used to create a neck measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the neck measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class ChestMeasurement(models.Model):
    """
    This class is used to create a chest measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the chest measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class WaistMeasurement(models.Model):
    """
    This class is used to create a waist measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the waist measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class ThighMeasurement(models.Model):
    """
    This class is used to create a thigh measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the thigh measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class ArmMeasurement(models.Model):
    """
    This class is used to create a arm measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the arm measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class CalfMeasurement(models.Model):
    """
    This class is used to create a calf measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the calf measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class ForearmMeasurement(models.Model):
    """
    This class is used to create a forearm measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the forearm measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class ShoulderMeasurement(models.Model):
    """
    This class is used to create a shoulder measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the shoulder measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class LovehandleMeasurement(models.Model):
    """
    This class is used to create a love handle measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the love handle measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class BeltMeasurement(models.Model):
    """
    This class is used to create a belt measurement model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    size = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the belt measurement.
        """
        return f"{self.user} measured {self.size}cm on {self.date}"


class WeightMeasurement(models.Model):
    """
    This class is used to create a weight record model.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        """
        This method returns the string representation of the weight record.
        """
        return f"{self.user} weighted {self.weight}kg on {self.date}"
