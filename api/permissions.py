from rest_framework import permissions


class IsAuthorOrReadOnly(
    permissions.BasePermission
):  # Custom permission for user authorization.
    def has_object_permission(self, request, view, obj):
        # Read-only permissions allowed for any request.
        if (
            request.method in permissions.SAFE_METHODS
        ):  # SAFE.METHODS contain GET-OPTIONS-HEAD etc.
            return True

        # Write permissions only allowed to the author of the post.
        return obj.accountant == request.user
