from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):
    """Is adim class."""

    def has_permission(self, request, view):
        """Only super users can create, edit and delete jobs. Normal users are allowed to only view Jobs."""
        if request.method in SAFE_METHODS:
            return request.user
        return request.user and request.user.is_staff
