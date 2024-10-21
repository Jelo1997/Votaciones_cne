from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from functools import wraps

def login_required_and_staff(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("No tienes permiso para acceder a esta página.")
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view