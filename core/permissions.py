from rest_framework.permissions import BasePermission


class DoctorAccessPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.user_type == 2)
