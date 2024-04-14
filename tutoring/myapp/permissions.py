
from rest_framework.permissions import BasePermission,SAFE_METHODS  # safe methods is a tuple containing  http methods(Get,Head,options)


class IsUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_staff==False))
    