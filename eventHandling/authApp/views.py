import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authApp.models import Role, User


# Create your views here.
@csrf_exempt
def register_user(request):
    try: 
        if request.method == 'POST':
            setData = json.loads(request.body) # Loading the JSON
            # print(setData)
            userName = setData.get('user_name')
            email = setData.get('email')
            password = setData.get('pass')
            role = setData.get('role')
            userRole = role # Assigning the Values that are entered by the user.
            user_role = Role.objects.filter(role_name=userRole)  # Filtering the Data whether found or not as written above
            if user_role.exists():
                user_role = user_role.first();  # If the Role is found in the database it will be then passed to the user_role which will later save to the User Table:
            else:
                user_role = Role.objects.create(role_name=userRole) # Otherwise new role is created, if failed to fetch from the database:
                user_role.save();
            user = User.objects.create(username=userName, email=email, password=password, role=user_role)
            if user is not None: 
                user.save();
            return JsonResponse({'message': 'User registered successfully', 'userName':user.username}) # Returning The JSON response once succeeded.
    except json.JSONDecodeError as error:
        return JsonResponse({'message': 'Error Loading the Json',
                             'status': str(error)}) # Error Wrapped in String:
    return JsonResponse({'message': 'Working'})