"""
This file is used to define the views of the core app.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from api.permissions import IsAdminOrOwner
from api.models import (
    CustomUser,
    NeckMeasurement,
    WaistMeasurement,
    WeightMeasurement,
    BeltMeasurement,
    LovehandleMeasurement,
    ThighMeasurement,
    CalfMeasurement,
    ArmMeasurement,
    ShoulderMeasurement,
    ChestMeasurement,
    ForearmMeasurement,
)
from api.serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    NeckDetailSerializer,
    WaistDetailSerializer,
    WeightDetailSerializer,
    BeltDetailSerializer,
    LovehandleDetailSerializer,
    ThighDetailSerializer,
    CalfDetailSerializer,
    ArmDetailSerializer,
    ShoulderDetailSerializer,
    ChestDetailSerializer,
    ForearmDetailSerializer,
)


# USER VIEWS


# -> Getting the list of all users
class UserListView(generics.ListAPIView):
    """
    Allows only admins to get the list of all users.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser]


# -> Getting the list of all weight measurements by user
class UserWeightMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all weight measurements.
    """

    serializer_class = WeightDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return WeightMeasurement.objects.filter(user=user)


# -> Getting the list of all chest measurements by user
class UserChestMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all chest measurements.
    """

    serializer_class = ChestDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return ChestMeasurement.objects.filter(user=user)


# -> Getting the list of all waist measurements by user
class UserWaistMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all waist measurements.
    """

    serializer_class = WaistDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return WaistMeasurement.objects.filter(user=user)


# -> Getting the list of all neck measurements by user
class UserNeckMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all neck measurements.
    """

    serializer_class = NeckDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return NeckMeasurement.objects.filter(user=user)


# -> Getting the list of all belt measurements by user
class UserBeltMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all belt measurements.
    """

    serializer_class = BeltDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return BeltMeasurement.objects.filter(user=user)


# -> Getting the list of all lovehandle measurements by user
class UserLovehandleMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all lovehandle measurements.
    """

    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return LovehandleMeasurement.objects.filter(user=user)


# -> Getting the list of all thigh measurements by user
class UserThighMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all thigh measurements.
    """

    serializer_class = ThighDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return ThighMeasurement.objects.filter(user=user)


# -> Getting the list of all calf measurements by user
class UserCalfMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all calf measurements.
    """

    serializer_class = CalfDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return CalfMeasurement.objects.filter(user=user)


# -> Getting the list of all arm measurements by user
class UserArmMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all arm measurements.
    """

    serializer_class = ArmDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return ArmMeasurement.objects.filter(user=user)


# -> Getting the list of all shoulder measurements by user
class UserShoulderMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all shoulder measurements.
    """

    serializer_class = ShoulderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return ShoulderMeasurement.objects.filter(user=user)


# -> Getting the list of all forearm measurements by user
class UserForearmMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all forearm measurements.
    """

    serializer_class = ForearmDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset by user.
        """
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return ForearmMeasurement.objects.filter(user=user)


# -> Creation of a new user
class UserCreateView(generics.CreateAPIView):
    """
    Allows unauthenticated users to create a new account.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


# -> Getting user data by ID
class UserDetailView(generics.RetrieveAPIView):
    """
    Allows authenticated users to get user data by ID.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users


# -> Getting the list of all users
class UserUpdateView(generics.UpdateAPIView):
    """
    Allows only admins or the user who owns the data to update their information using pk.
    """

    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        """
        Return a queryset for the user by primary key.
        """
        return CustomUser.objects.filter(pk=self.kwargs["pk"])

    def get_object(self):
        """
        Retrieve and return the user by the primary key (pk).
        """
        return generics.get_object_or_404(CustomUser, pk=self.kwargs["pk"])


# -> Deleting user data by ID
class UserDeleteView(generics.DestroyAPIView):
    """
    Allows only admins or the user who owns the data to delete their information using pk.
    """

    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        """
        Return a queryset for the user by primary key.
        """
        return CustomUser.objects.filter(pk=self.kwargs["pk"])

    def get_object(self):
        """
        Retrieve and return the user by the primary key (pk).
        """
        return generics.get_object_or_404(CustomUser, pk=self.kwargs["pk"])


# NECK MEASUREMENT VIEWS


# -> Getting the list of all neck measurements
class NeckMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all neck measurements.
    """

    queryset = NeckMeasurement.objects.all()
    serializer_class = NeckDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new neck measurement
class NeckMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new neck measurement.
    """

    queryset = NeckMeasurement.objects.all()
    serializer_class = NeckDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting neck measurement data by ID
class NeckMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get neck measurement data by ID.
    """

    queryset = NeckMeasurement.objects.all()
    serializer_class = NeckDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating neck measurement data by ID
class NeckMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update neck measurement data by ID.
    """

    queryset = NeckMeasurement.objects.all()
    serializer_class = NeckDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting neck measurement data by ID
class NeckMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete neck measurement data by ID.
    """

    queryset = NeckMeasurement.objects.all()
    serializer_class = NeckDetailSerializer
    permission_classes = [IsAuthenticated]


# WAIST MEASUREMENT VIEWS


# -> Getting the list of all waist measurements
class WaistMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all waist measurements.
    """

    queryset = WaistMeasurement.objects.all()
    serializer_class = WaistDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new waist measurement
class WaistMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new waist measurement.
    """

    queryset = WaistMeasurement.objects.all()
    serializer_class = WaistDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting waist measurement data by ID
class WaistMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get waist measurement data by ID.
    """

    queryset = WaistMeasurement.objects.all()
    serializer_class = WaistDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating waist measurement data by ID
class WaistMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update waist measurement data by ID.
    """

    queryset = WaistMeasurement.objects.all()
    serializer_class = WaistDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting waist measurement data by ID
class WaistMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete waist measurement data by ID.
    """

    queryset = WaistMeasurement.objects.all()
    serializer_class = WaistDetailSerializer
    permission_classes = [IsAuthenticated]


# WEIGHT MEASUREMENT VIEWS


# -> Getting the list of all weight measurement
class WeightMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all weight measurement.
    """

    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new weight measurement
class WeightMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new weight measurement.
    """

    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting weight measurement data by ID
class WeightMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get weight measurement data by ID.
    """

    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating weight measurement data by ID
class WeightMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update weight measurement data by ID.
    """

    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting weight measurement data by ID
class WeightMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete weight measurement data by ID.
    """

    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightDetailSerializer
    permission_classes = [IsAuthenticated]


# BELT MEASUREMENT VIEWS


# -> Getting the list of all belt measurements
class BeltMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all belt measurements.
    """

    queryset = BeltMeasurement.objects.all()
    serializer_class = BeltDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new belt measurement
class BeltMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new belt measurement.
    """

    queryset = BeltMeasurement.objects.all()
    serializer_class = BeltDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting belt measurement data by ID
class BeltMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get belt measurement data by ID.
    """

    queryset = BeltMeasurement.objects.all()
    serializer_class = BeltDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating belt measurement data by ID
class BeltMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update belt measurement data by ID.
    """

    queryset = BeltMeasurement.objects.all()
    serializer_class = BeltDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting belt measurement data by ID
class BeltMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete belt measurement data by ID.
    """

    queryset = BeltMeasurement.objects.all()
    serializer_class = BeltDetailSerializer
    permission_classes = [IsAuthenticated]


# LOVEHANDLE MEASUREMENT VIEWS


# -> Getting the list of all lovehandle measurements
class LovehandleMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all lovehandle measurements.
    """

    queryset = LovehandleMeasurement.objects.all()
    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new lovehandle measurement
class LovehandleMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new lovehandle measurement.
    """

    queryset = LovehandleMeasurement.objects.all()
    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting lovehandle measurement data by ID
class LovehandleMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get lovehandle measurement data by ID.
    """

    queryset = LovehandleMeasurement.objects.all()
    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating lovehandle measurement data by ID
class LovehandleMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update lovehandle measurement data by ID.
    """

    queryset = LovehandleMeasurement.objects.all()
    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting lovehandle measurement data by ID
class LovehandleMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete lovehandle measurement data by ID.
    """

    queryset = LovehandleMeasurement.objects.all()
    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]


# THIGH MEASUREMENT VIEWS


# -> Getting the list of all thigh measurements
class ThighMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all thigh measurements.
    """

    queryset = ThighMeasurement.objects.all()
    serializer_class = LovehandleDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new thigh measurement
class ThighMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new thigh measurement.
    """

    queryset = ThighMeasurement.objects.all()
    serializer_class = ThighDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting thigh measurement data by ID
class ThighMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get thigh measurement data by ID.
    """

    queryset = ThighMeasurement.objects.all()
    serializer_class = ThighDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating thigh measurement data by ID
class ThighMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update thigh measurement data by ID.
    """

    queryset = ThighMeasurement.objects.all()
    serializer_class = ThighDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting thigh measurement data by ID
class ThighMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete thigh measurement data by ID.
    """

    queryset = ThighMeasurement.objects.all()
    serializer_class = ThighDetailSerializer
    permission_classes = [IsAuthenticated]


# CALF MEASUREMENT VIEWS


# -> Getting the list of all calf measurements
class CalfMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all calf measurements.
    """

    queryset = CalfMeasurement.objects.all()
    serializer_class = CalfDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new calf measurement
class CalfMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new calf measurement.
    """

    queryset = CalfMeasurement.objects.all()
    serializer_class = CalfDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting calf measurement data by ID
class CalfMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get calf measurement data by ID.
    """

    queryset = CalfMeasurement.objects.all()
    serializer_class = CalfDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating calf measurement data by ID
class CalfMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update calf measurement data by ID.
    """

    queryset = CalfMeasurement.objects.all()
    serializer_class = CalfDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting calf measurement data by ID
class CalfMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete calf measurement data by ID.
    """

    queryset = CalfMeasurement.objects.all()
    serializer_class = CalfDetailSerializer
    permission_classes = [IsAuthenticated]


# ARM MEASUREMENT VIEWS


# -> Getting the list of all arm measurements
class ArmMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all arm measurements.
    """

    queryset = ArmMeasurement.objects.all()
    serializer_class = ArmDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new arm measurement
class ArmMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new arm measurement.
    """

    queryset = ArmMeasurement.objects.all()
    serializer_class = ArmDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting arm measurement data by ID
class ArmMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get arm measurement data by ID.
    """

    queryset = ArmMeasurement.objects.all()
    serializer_class = ArmDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating arm measurement data by ID
class ArmMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update arm measurement data by ID.
    """

    queryset = ArmMeasurement.objects.all()
    serializer_class = ArmDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting arm measurement data by ID
class ArmMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete arm measurement data by ID.
    """

    queryset = ArmMeasurement.objects.all()
    serializer_class = ArmDetailSerializer
    permission_classes = [IsAuthenticated]


# SHOULDER MEASUREMENT VIEWS


# -> Getting the list of all shoulder measurements
class ShoulderMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all shoulder measurements.
    """

    queryset = ShoulderMeasurement.objects.all()
    serializer_class = ShoulderDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new shoulder measurement
class ShoulderMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new shoulder measurement.
    """

    queryset = ShoulderMeasurement.objects.all()
    serializer_class = ShoulderDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting shoulder measurement data by ID
class ShoulderMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get shoulder measurement data by ID.
    """

    queryset = ShoulderMeasurement.objects.all()
    serializer_class = ShoulderDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating shoulder measurement data by ID
class ShoulderMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update shoulder measurement data by ID.
    """

    queryset = ShoulderMeasurement.objects.all()
    serializer_class = ShoulderDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting shoulder measurement data by ID
class ShoulderMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete shoulder measurement data by ID.
    """

    queryset = ShoulderMeasurement.objects.all()
    serializer_class = ShoulderDetailSerializer
    permission_classes = [IsAuthenticated]


# CHEST MEASUREMENT VIEWS


# -> Getting the list of all chest measurements
class ChestMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all chest measurements.
    """

    queryset = ChestMeasurement.objects.all()
    serializer_class = ChestDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new chest measurement
class ChestMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new chest measurement.
    """

    queryset = ChestMeasurement.objects.all()
    serializer_class = ChestDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting chest measurement data by ID
class ChestMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get chest measurement data by ID.
    """

    queryset = ChestMeasurement.objects.all()
    serializer_class = ChestDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating chest measurement data by ID
class ChestMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update chest measurement data by ID.
    """

    queryset = ChestMeasurement.objects.all()
    serializer_class = ChestDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting chest measurement data by ID
class ChestMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete chest measurement data by ID.
    """

    queryset = ChestMeasurement.objects.all()
    serializer_class = ChestDetailSerializer
    permission_classes = [IsAuthenticated]


# FOREARM MEASUREMENT VIEWS


# -> Getting the list of all forearm measurements
class ForearmMeasurementListView(generics.ListCreateAPIView):
    """
    Allows only authenticated users to get the list of all forearm measurements.
    """

    queryset = ForearmMeasurement.objects.all()
    serializer_class = ForearmDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Creation of a new forearm measurement
class ForearmMeasurementCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create a new forearm measurement.
    """

    queryset = ForearmMeasurement.objects.all()
    serializer_class = ForearmDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically set the user field to the authenticated user when saving the measurement.
        """
        if self.request.user and not self.request.user.is_anonymous:
            print(f"Authenticated user: {self.request.user}")  # Debugging
            serializer.save(user=self.request.user)
        else:
            raise ValidationError("User is not authenticated.")


# -> Getting forearm measurement data by ID
class ForearmMeasurementDetailView(generics.RetrieveAPIView):
    """
    Allows only authenticated users to get forearm measurement data by ID.
    """

    queryset = ForearmMeasurement.objects.all()
    serializer_class = ForearmDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Updating forearm measurement data by ID
class ForearmMeasurementUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update forearm measurement data by ID.
    """

    queryset = ForearmMeasurement.objects.all()
    serializer_class = ForearmDetailSerializer
    permission_classes = [IsAuthenticated]


# -> Deleting forearm measurement data by ID
class ForearmMeasurementDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete forearm measurement data by ID.
    """

    queryset = ForearmMeasurement.objects.all()
    serializer_class = ForearmDetailSerializer
    permission_classes = [IsAuthenticated]
