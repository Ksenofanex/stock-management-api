from rest_framework import permissions


class IsAccountantOrReadOnly(
    permissions.BasePermission
):  # Custom permission for accountant authorization.
    def has_object_permission(self, request, view, obj):
        if (
            request.method in permissions.SAFE_METHODS
        ):  # SAFE.METHODS contain GET-OPTIONS-HEAD etc.
            return True

        # Write permissions only allowed to the accountant of the stock.
        return obj.accountant == request.user
