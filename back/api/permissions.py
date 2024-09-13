"""
Custom permissions for the API.
"""

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a weight record to access it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the current user is the owner of the weight record.
        """
        return obj.user == request.user


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow admins or the owner of the object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is an admin or the owner of the object.
        """
        if request.user.is_staff:
            return True
        return obj == request.user
