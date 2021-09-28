from rest_framework.permissions import BasePermission
from .models import Pomo


class IsOwner(BasePermission):
    """Custom permission class to allow only pomo owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the pomo owner."""
        if isinstance(obj, Pomo):
            return obj.owner == request.user
        return obj.owner == request.user