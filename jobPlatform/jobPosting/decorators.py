from functools import wraps
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # ADAPT THIS: Change 'request.user.role' to match your actual model logic
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def recruiter_required(view_func):
    
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # ADAPT THIS: Change 'request.user.role' to match your actual model logic
        if request.user.is_authenticated and request.user.role == 'recruiter':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def employee_required(view_func):
    
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # ADAPT THIS: Change 'request.user.role' to match your actual model logic
        if request.user.is_authenticated and request.user.role == 'employee':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view