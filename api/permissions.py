from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import User

class IsAdminICTOrResearcherReadUpdate(BasePermission):
    """
   Permissions:
    - Admin & ICT: full CRUD
    - Researcher: GET + PUT/PATCH
    - Other users: GET only
    """

    def has_permission(self, request, view):
        user = request.user

        # Anonymous user
        if not user.is_authenticated:
            return request.method in SAFE_METHODS

        # Admin & ICT → Full access
        if user.role in [User.ROLE_ADMIN, User.ROLE_ICT]:
            return True

        # Researcher → GET + PUT/PATCH
        if user.role == User.ROLE_RESEARCHER:
            return request.method in SAFE_METHODS + ("PUT", "PATCH")

        # Regular user → GET only
        if user.role == User.ROLE_USER:
            return request.method in SAFE_METHODS

        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_ADMIN
        )


class IsICT(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [User.ROLE_ADMIN, User.ROLE_ICT]
        )


class IsResearcher(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.ROLE_ADMIN,
                User.ROLE_ICT,
                User.ROLE_RESEARCHER,
            ]
        )