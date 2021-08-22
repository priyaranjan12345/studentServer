from rest_framework import permissions
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication

class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if (user.is_authenticated):
            if(user.is_superuser):
                return True
            else:
                return False
        else:
            return False

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if (user.is_authenticated):
            return True
        else:
            return False
        