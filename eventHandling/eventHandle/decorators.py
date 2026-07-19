from functools import wraps
from django.http import JsonResponse

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Perform the role check directly using the request.user
        if hasattr(request.user, 'role') and request.user.role.role_name == 'isAdmin':
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({
                'Status': 'Unauthorized',
                'Message': 'Only Admins can perform this action.'
            }, status=403)
    return _wrapped_view