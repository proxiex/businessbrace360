from rest_framework.permissions import BasePermission


class IsSuperUserOrWriteRetriveOnly(BasePermission):
    """Is adim class."""

    def has_permission(self, request, view):
        """Only super users can view all, edit and delete dashboard. Normal users are allowed to only view and Create."""

        # if request.method in new_safe_methods:
        if view.action in ('retrieve', 'create',):
            return request.user and request.user.is_authenticated
        else:
            return request.user and request.user.is_staff

