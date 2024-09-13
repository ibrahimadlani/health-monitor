"""
This file is used to define the urls of the core app.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import (
    UserListView,
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserWeightMeasurementListView,
    UserWaistMeasurementListView,
    UserBeltMeasurementListView,
    UserLovehandleMeasurementListView,
    UserThighMeasurementListView,
    UserCalfMeasurementListView,
    UserForearmMeasurementListView,
    UserArmMeasurementListView,
    UserShoulderMeasurementListView,
    UserChestMeasurementListView,
    WeightMeasurementListView,
    WeightMeasurementCreateView,
    WeightMeasurementDetailView,
    WeightMeasurementUpdateView,
    WeightMeasurementDeleteView,
    NeckMeasurementListView,
    NeckMeasurementCreateView,
    NeckMeasurementDetailView,
    NeckMeasurementUpdateView,
    NeckMeasurementDeleteView,
    WaistMeasurementListView,
    WaistMeasurementCreateView,
    WaistMeasurementDetailView,
    WaistMeasurementUpdateView,
    WaistMeasurementDeleteView,
    BeltMeasurementListView,
    BeltMeasurementCreateView,
    BeltMeasurementDetailView,
    BeltMeasurementUpdateView,
    BeltMeasurementDeleteView,
    LovehandleMeasurementListView,
    LovehandleMeasurementCreateView,
    LovehandleMeasurementDetailView,
    LovehandleMeasurementUpdateView,
    LovehandleMeasurementDeleteView,
    ThighMeasurementListView,
    ThighMeasurementCreateView,
    ThighMeasurementDetailView,
    ThighMeasurementUpdateView,
    ThighMeasurementDeleteView,
    CalfMeasurementListView,
    CalfMeasurementCreateView,
    CalfMeasurementDetailView,
    CalfMeasurementUpdateView,
    CalfMeasurementDeleteView,
    ForearmMeasurementListView,
    ForearmMeasurementCreateView,
    ForearmMeasurementDetailView,
    ForearmMeasurementUpdateView,
    ForearmMeasurementDeleteView,
    ArmMeasurementListView,
    ArmMeasurementCreateView,
    ArmMeasurementDetailView,
    ArmMeasurementUpdateView,
    ArmMeasurementDeleteView,
    ShoulderMeasurementListView,
    ShoulderMeasurementCreateView,
    ShoulderMeasurementDetailView,
    ShoulderMeasurementUpdateView,
    ShoulderMeasurementDeleteView,
    ChestMeasurementListView,
    ChestMeasurementCreateView,
    ChestMeasurementDetailView,
    ChestMeasurementUpdateView,
    ChestMeasurementDeleteView,
)

urlpatterns = [
    # [AUTHENTICATION]
    ## Get token
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    ## Refresh token
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # [USERS]
    ## List users
    path("users/", UserListView.as_view(), name="user-list"),
    ## Create user
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    ## Read user
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    ## Update user
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    ## Delete user
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    ## Get user neck measurements
    path(
        "users/<int:pk>/neck/",
        NeckMeasurementListView.as_view(),
        name="user-neck-measurement-list",
    ),
    ## Get user weights measurements
    path(
        "users/<int:pk>/weights/",
        UserWeightMeasurementListView.as_view(),
        name="user-weight-measurement-list",
    ),
    ## Get user waist measurements
    path(
        "users/<int:pk>/waist/",
        UserWaistMeasurementListView.as_view(),
        name="user-waist-measurement-list",
    ),
    ## Get user belt measurements
    path(
        "users/<int:pk>/belt/",
        UserBeltMeasurementListView.as_view(),
        name="user-belt-measurement-list",
    ),
    ## Get user lovehandle measurements
    path(
        "users/<int:pk>/lovehandle/",
        UserLovehandleMeasurementListView.as_view(),
        name="user-lovehandle-measurement-list",
    ),
    ## Get user thigh measurements
    path(
        "users/<int:pk>/thigh/",
        UserThighMeasurementListView.as_view(),
        name="user-thigh-measurement-list",
    ),
    ## Get user calves measurements
    path(
        "users/<int:pk>/calves/",
        UserCalfMeasurementListView.as_view(),
        name="user-calves-measurement-list",
    ),
    ## Get user forearm measurements
    path(
        "users/<int:pk>/forearm/",
        UserForearmMeasurementListView.as_view(),
        name="user-forearm-measurement-list",
    ),
    ## Get user arm measurements
    path(
        "users/<int:pk>/arm/",
        UserArmMeasurementListView.as_view(),
        name="user-arm-measurement-list",
    ),
    ## Get user shoulder measurements
    path(
        "users/<int:pk>/shoulder/",
        UserShoulderMeasurementListView.as_view(),
        name="user-shoulder-measurement-list",
    ),
    ## Get user chest measurements
    path(
        "users/<int:pk>/chest/",
        UserChestMeasurementListView.as_view(),
        name="user-chest-measurement-list",
    ),
    # [WEIGHTS]
    ## List weight measurements
    path(
        "weights/", WeightMeasurementListView.as_view(), name="weight-measurements-list"
    ),
    ## Create weight measurements
    path(
        "weights/create/",
        WeightMeasurementCreateView.as_view(),
        name="weight-measurements-create",
    ),
    ## Read weight measurements
    path(
        "weights/<int:pk>/",
        WeightMeasurementDetailView.as_view(),
        name="weight-measurements-detail",
    ),
    ## Update weight measurements
    path(
        "weights/<int:pk>/update/",
        WeightMeasurementUpdateView.as_view(),
        name="weight-measurements-update",
    ),
    ## Delete weight measurements
    path(
        "weights/<int:pk>/delete/",
        WeightMeasurementDeleteView.as_view(),
        name="weight-measurements-delete",
    ),
    # NECK MEASUREMENTS]
    ## List neck measurements
    path("neck/", NeckMeasurementListView.as_view(), name="neck-measurement-list"),
    ## Create neck measurement
    path(
        "neck/create/",
        NeckMeasurementCreateView.as_view(),
        name="neck-measurement-create",
    ),
    ## Read neck measurement
    path(
        "neck/<int:pk>/",
        NeckMeasurementDetailView.as_view(),
        name="neck-measurement-detail",
    ),
    ## Update neck measurement
    path(
        "neck/<int:pk>/update/",
        NeckMeasurementUpdateView.as_view(),
        name="neck-measurement-update",
    ),
    ## Delete neck measurement
    path(
        "neck/<int:pk>/delete/",
        NeckMeasurementDeleteView.as_view(),
        name="neck-measurement-delete",
    ),
    # [WAIST MEASUREMENTS]
    ## List waist measurements
    path("waist/", WaistMeasurementListView.as_view(), name="waist-measurement-list"),
    ## Create waist measurement
    path(
        "waist/create/",
        WaistMeasurementCreateView.as_view(),
        name="waist-measurement-create",
    ),
    ## Read waist measurement
    path(
        "waist/<int:pk>/",
        WaistMeasurementDetailView.as_view(),
        name="waist-measurement-detail",
    ),
    ## Update waist measurement
    path(
        "waist/<int:pk>/update/",
        WaistMeasurementUpdateView.as_view(),
        name="waist-measurement-update",
    ),
    ## Delete waist measurement
    path(
        "waist/<int:pk>/delete/",
        WaistMeasurementDeleteView.as_view(),
        name="waist-measurement-delete",
    ),
    # [BELT MEASUREMENTS]
    ## List belt measurements
    path("belt/", BeltMeasurementListView.as_view(), name="belt-measurement-list"),
    ## Create belt measurement
    path(
        "belt/create/",
        BeltMeasurementCreateView.as_view(),
        name="belt-measurement-create",
    ),
    ## Read belt measurement
    path(
        "belt/<int:pk>/",
        BeltMeasurementDetailView.as_view(),
        name="belt-measurement-detail",
    ),
    ## Update belt measurement
    path(
        "belt/<int:pk>/update/",
        BeltMeasurementUpdateView.as_view(),
        name="belt-measurement-update",
    ),
    ## Delete belt measurement
    path(
        "belt/<int:pk>/delete/",
        BeltMeasurementDeleteView.as_view(),
        name="belt-measurement-delete",
    ),
    # [LOVEHANDLE MEASUREMENTS]
    ## List lovehandle measurements
    path(
        "lovehandle/",
        LovehandleMeasurementListView.as_view(),
        name="lovehandle-measurement-list",
    ),
    ## Create lovehandle measurement
    path(
        "lovehandle/create/",
        LovehandleMeasurementCreateView.as_view(),
        name="lovehandle-measurement-create",
    ),
    ## Read lovehandle measurement
    path(
        "lovehandle/<int:pk>/",
        LovehandleMeasurementDetailView.as_view(),
        name="lovehandle-measurement-detail",
    ),
    ## Update lovehandle measurement
    path(
        "lovehandle/<int:pk>/update/",
        LovehandleMeasurementUpdateView.as_view(),
        name="lovehandle-measurement-update",
    ),
    ## Delete lovehandle measurement
    path(
        "lovehandle/<int:pk>/delete/",
        LovehandleMeasurementDeleteView.as_view(),
        name="lovehandle-measurement-delete",
    ),
    # [THIGH MEASUREMENTS]
    ## List thigh measurements
    path("thigh/", ThighMeasurementListView.as_view(), name="thigh-measurement-list"),
    ## Create thigh measurement
    path(
        "thigh/create/",
        ThighMeasurementCreateView.as_view(),
        name="thigh-measurement-create",
    ),
    ## Read thigh measurement
    path(
        "thigh/<int:pk>/",
        ThighMeasurementDetailView.as_view(),
        name="thigh-measurement-detail",
    ),
    ## Update thigh measurement
    path(
        "thigh/<int:pk>/update/",
        ThighMeasurementUpdateView.as_view(),
        name="thigh-measurement-update",
    ),
    ## Delete thigh measurement
    path(
        "thigh/<int:pk>/delete/",
        ThighMeasurementDeleteView.as_view(),
        name="thigh-measurement-delete",
    ),
    # [CALVES MEASUREMENTS]
    ## List calves measurements
    path("calves/", CalfMeasurementListView.as_view(), name="calves-measurement-list"),
    ## Create calves measurement
    path(
        "calves/create/",
        CalfMeasurementCreateView.as_view(),
        name="calves-measurement-create",
    ),
    ## Read calves measurement
    path(
        "calves/<int:pk>/",
        CalfMeasurementDetailView.as_view(),
        name="calves-measurement-detail",
    ),
    ## Update calves measurement
    path(
        "calves/<int:pk>/update/",
        CalfMeasurementUpdateView.as_view(),
        name="calves-measurement-update",
    ),
    ## Delete calves measurement
    path(
        "calves/<int:pk>/delete/",
        CalfMeasurementDeleteView.as_view(),
        name="calves-measurement-delete",
    ),
    # [FOREARM MEASUREMENTS]
    ## List forearm measurements
    path(
        "forearm/",
        ForearmMeasurementListView.as_view(),
        name="forearm-measurement-list",
    ),
    ## Create forearm measurement
    path(
        "forearm/create/",
        ForearmMeasurementCreateView.as_view(),
        name="forearm-measurement-create",
    ),
    ## Read forearm measurement
    path(
        "forearm/<int:pk>/",
        ForearmMeasurementDetailView.as_view(),
        name="forearm-measurement-detail",
    ),
    ## Update forearm measurement
    path(
        "forearm/<int:pk>/update/",
        ForearmMeasurementUpdateView.as_view(),
        name="forearm-measurement-update",
    ),
    ## Delete forearm measurement
    path(
        "forearm/<int:pk>/delete/",
        ForearmMeasurementDeleteView.as_view(),
        name="forearm-measurement-delete",
    ),
    # [ARM MEASUREMENTS]
    ## List arm measurements
    path("arm/", ArmMeasurementListView.as_view(), name="arm-measurement-list"),
    ## Create arm measurement
    path(
        "arm/create/", ArmMeasurementCreateView.as_view(), name="arm-measurement-create"
    ),
    ## Read arm measurement
    path(
        "arm/<int:pk>/",
        ArmMeasurementDetailView.as_view(),
        name="arm-measurement-detail",
    ),
    ## Update arm measurement
    path(
        "arm/<int:pk>/update/",
        ArmMeasurementUpdateView.as_view(),
        name="arm-measurement-update",
    ),
    ## Delete arm measurement
    path(
        "arm/<int:pk>/delete/",
        ArmMeasurementDeleteView.as_view(),
        name="arm-measurement-delete",
    ),
    # [SHOULDER MEASUREMENTS]
    ## List shoulder measurements
    path(
        "shoulder/",
        ShoulderMeasurementListView.as_view(),
        name="shoulder-measurement-list",
    ),
    ## Create shoulder measurement
    path(
        "shoulder/create/",
        ShoulderMeasurementCreateView.as_view(),
        name="shoulder-measurement-create",
    ),
    ## Read shoulder measurement
    path(
        "shoulder/<int:pk>/",
        ShoulderMeasurementDetailView.as_view(),
        name="shoulder-measurement-detail",
    ),
    ## Update shoulder measurement
    path(
        "shoulder/<int:pk>/update/",
        ShoulderMeasurementUpdateView.as_view(),
        name="shoulder-measurement-update",
    ),
    ## Delete shoulder measurement
    path(
        "shoulder/<int:pk>/delete/",
        ShoulderMeasurementDeleteView.as_view(),
        name="shoulder-measurement-delete",
    ),
    # [CHEST MEASUREMENTS]
    ## List chest measurements
    path("chest/", ChestMeasurementListView.as_view(), name="chest-measurement-list"),
    ## Create chest measurement
    path(
        "chest/create/",
        ChestMeasurementCreateView.as_view(),
        name="chest-measurement-create",
    ),
    ## Read chest measurement
    path(
        "chest/<int:pk>/",
        ChestMeasurementDetailView.as_view(),
        name="chest-measurement-detail",
    ),
    ## Update chest measurement
    path(
        "chest/<int:pk>/update/",
        ChestMeasurementUpdateView.as_view(),
        name="chest-measurement-update",
    ),
    ## Delete chest measurement
    path(
        "chest/<int:pk>/delete/",
        ChestMeasurementDeleteView.as_view(),
        name="chest-measurement-delete",
    ),
]
