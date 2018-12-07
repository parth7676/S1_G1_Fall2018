from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from myapp.models import UserRole


def admin_only(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not isinstance(user, AnonymousUser):
            roles = UserRole.objects.filter(user__userID=user.userID).select_related('role').all()
            for role in roles:
                if 'ADMIN' == role.role.code:
                    return function(request, *args, **kwargs)
            raise PermissionDenied
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
