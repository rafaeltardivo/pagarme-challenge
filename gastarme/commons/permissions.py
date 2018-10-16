from rest_framework.permissions import BasePermission, IsAuthenticated


class IsSuperUser(BasePermission):
    """Permission class for superusers."""

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsRegularUser(BasePermission):
    """Permission class for regular users only."""

    def has_permission(self, request, view):
        return request.user and IsAuthenticated and not \
            request.user.is_superuser


class IsUserCresteListOrSuperuserListDelete(BasePermission):
    """Permission class for superusers (list, delete) or users(create, list)."""
    SUPERUSER_ACTIONS = ['GET', 'DELETE']
    USER_ACTIONS = ['GET', 'POST']

    def has_permission(self, request, view):
        is_superuser = request.user and request.user.is_superuser

        superuser_allowed = is_superuser and \
            request.method in self.SUPERUSER_ACTIONS

        user_allowed = not is_superuser and \
            IsAuthenticated() and request.method in self.USER_ACTIONS

        return superuser_allowed or user_allowed
