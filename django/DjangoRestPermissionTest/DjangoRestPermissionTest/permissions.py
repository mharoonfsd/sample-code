"""Custom permissions for the DjangoRestPermissionTest base project."""

from rest_framework import permissions

from DjangoRestPermissionTest.models import TestModel


ALLOWED_USERNAMES = ['aaron']

class TestModelPermission(permissions.BasePermission):
    """Permission to perform custom checks."""

    def has_permission(self, request, view):
        """Chack if the user is allowed to list objects."""
        if view.action in ['list', 'retrieve']:
            return request.user and request.user.is_staff
        elif view.action == 'create':
            return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        """Chack if the user is allowed to create or update objects."""
        print(request.user.is_superuser)
        if (view.action in ['create', 'update', 'partial_update', 'destroy']
            and request.user.is_superuser
            and self.check_legal(obj)):
            return True
        return False

    def check_legal(self, obj):
        """Check if object is legal."""
        if (hasattr(obj.__class__, obj.col1.upper())
            and isinstance(getattr(obj.__class__, obj.col1.upper()), str)):
            return True
        return False


class TestRelationModelPermission(permissions.BasePermission):
    """Permission to perform custom checks on relational model."""

    def has_permission(self, request, view):
        """Chack if the user is allowed to list objects."""
        if (hasattr(TestModel, view.item.upper())
            and request.user.is_superuser):
            return True
        return False