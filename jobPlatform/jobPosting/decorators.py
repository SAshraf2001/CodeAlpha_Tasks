from functools import wraps
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # We filter the user's role relationship to see if 'admin' exists within it
        if request.user.is_authenticated and request.user.role.filter(roleName='admin').exists():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def recruiter_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role.filter(roleName='recruiter').exists():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def employee_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # This replaces the '==' check with a database query that returns True/False
        if request.user.is_authenticated and request.user.role.filter(roleName='employee').exists():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view