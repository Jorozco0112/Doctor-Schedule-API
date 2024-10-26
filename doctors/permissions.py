from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    """This is a personalized permission"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='doctors').exists()
