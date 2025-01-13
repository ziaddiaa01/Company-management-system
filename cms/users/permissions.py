from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows full access to Admin users only.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Admin'


class IsManagerOrReadOnly(BasePermission):
    """
    Allows read-only access to all, but only Managers can update data.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user.is_authenticated and request.user.role == 'Manager'


class IsEmployeeReadOnly(BasePermission):
    """
    Allows employees to view their own data only.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return request.user.is_authenticated and obj == request.user
        return False
