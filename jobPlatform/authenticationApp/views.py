import json
from django.shortcuts import render
from authenticationApp.models import User, Role
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def registeredUser(request):
    try:
        if request.method == 'POST':
            setData = json.loads(request.body)
            userName = setData.get('User Name')
            email = setData.get('email')
            password = setData.get('Password')
            userRole = setData.get('User Role')
            
            #user_role, created = Role.objects.get_or_create(roleName = userRole)
            #role = Role.objects.create(roleName=user_role)
            
            user_role = Role.objects.filter(roleName = userRole)
            if user_role.exists():
                user_role = user_role.first()
            else: 
                user_role = Role.objects.create(roleName=userRole)
            user = User.objects.create(role=user_role)
            user.username = userName # Extracting the User Name from the Input and passing it to the builtIn username.
            user.email = email
            user.set_password(password)
            user.save()
            
            return JsonResponse({
                'Status': 'User is Registered',
                'User Name': userName,
                'Email': email,
                'Role': userRole
            })
    except json.JSONDecodeError as err:
        return JsonResponse({
            'Status': 'Failed',
            'Message': f"Exception Caught ---> Error:{str(err)}"
        })    
        
    return JsonResponse({
        'Status': 'Passed and Completed',
        'Message': 'URL is working.'
    })