import json
from django.shortcuts import render
from django.http import JsonResponse
from authApp.models import Role, User


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        setData = json.loads(request.body)
        print(setData)
        userName = setData.get('user_name')
        email = setData.get('email')
        password = setData.get('pass')
        role = setData.get('role')
        userRole = role
        user_role = Role.objects.filter(role_name=userRole)
        if user_role.exists():
            pass
        else:
            user_role = Role.objects.create(role_name=userRole)
            user_role.save();
        user = User.objects.create(username=userName, email=email, password=password, role=user_role)
        if user is not None: 
            user.save();
        
    return JsonResponse({'message': 'User registered successfully'})