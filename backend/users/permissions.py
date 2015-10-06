from rest_framework import permissions


class TwoFactorIsVerified(permissions.IsAuthenticated):
    """
        Allow access only to two factor verified users
    """
    def has_permission(self, request, view):
        super(TwoFactorIsVerified, self).has_permission(request, view)
        return request.user.is_verified()
