from functools import wraps
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Checks if user is logged in, has a role assigned, and that role is 'isAdmin'
        if (request.user.is_authenticated and 
            request.user.role and 
            request.user.role.roleName == 'isAdmin'):
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Checks if user is logged in, has a role assigned, and that role is 'isRecruiter'
        allowed_roles=['isAdmin', 'isRecruiter']
        if (request.user.is_authenticated and 
            request.user.role and 
            request.user.role.roleName in allowed_roles):
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def employee_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Checks if user is logged in, has a role assigned, and that role is 'isEmployee'
        if (request.user.is_authenticated and 
            request.user.role and 
            request.user.role.roleName == 'isEmployee'):
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view