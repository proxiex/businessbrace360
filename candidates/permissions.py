from rest_framework.permissions import BasePermission


class IsSuperUserOrWriteOnly(BasePermission):
    """Is adim class."""

    def has_permission(self, request, view):
        """Only super users can edit and delete Candidates. Normal users are allowed to only view and Create ."""
        new_safe_methods = ('POST', 'HEAD', 'OPTIONS')

        if request.method in new_safe_methods:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
