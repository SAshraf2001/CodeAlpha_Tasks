import json
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authApp.models import Role, User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404


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
            user = User.objects.create_user(username=userName, email=email, password=password, role=user_role) # Created the User by using builtin create_user
            user.set_password(password) # Saving the Password in raw numbers instead of String:
            if user is not None: 
                user.save();
            return JsonResponse({'message': 'User registered successfully', 'userName':user.username}) # Returning The JSON response once succeeded.
    except json.JSONDecodeError as error:
        return JsonResponse({'message': 'Error Loading the Json',
                             'status': str(error)}) # Error Wrapped in String:
    return JsonResponse({'message': 'Working'})

@csrf_exempt
def login_user(request):
    try: 
        if request.method == 'POST':
            setLoginData = json.loads(request.body)
            loginUserName = setLoginData.get('user_name')
            loginPassword = setLoginData.get('pass')
            loginRole = setLoginData.get('role')
            user_role = Role.objects.filter(role_name=loginRole).first()
            
            # if user_role is not None:
            #     return JsonResponse({
            #         'status': 'Role is Fetched: {user_role}'
            #     })
            
            
            if((not loginUserName) or (not loginPassword) or (not user_role)):
                return JsonResponse({
                    'status': 'No User Found, Try Again',
                    'Role Status': f"No Role is Found Also Try Again: {user_role}"
                    })
            else: 
                user = authenticate(username=loginUserName, password=loginPassword)
                if user is not None:
                    login(request, user)
                    return JsonResponse({
                        'status': 'Login Confirmed, User is Loggedin Successfully:',
                        'User_name': user.username, 
                        'Role Status': f'Role: {user_role}'
                    })
                else: 
                    return JsonResponse({'message': "You must Signup or Register to be Logged In:"})
    except json.JSONDecodeError as error:
        return JsonResponse({
            'Status': "JSON couldn't load",
            'Error': str(error)
        })
    return JsonResponse({'message': 'Working Fine:'})

@csrf_exempt
def logout_user(request):
    try:
        if request.method == 'POST':
            
            if request.user.is_authenticated: # Checking whether the user is Logged In 
                
                # print(f'User Found --> {request.user.username}') # Throwing the Name of the Current Logged In user
                logged_user = request.user.username # Storing the name into the variable
                logout(request)
                
                return JsonResponse({
                'message': 'User has been Logged Out',
                'User': logged_user
                })
            else:
                return JsonResponse({'status': 'NO user found:'})    
    except json.JSONDecodeError as error:
        return JsonResponse({
            "status": error
        })
    return JsonResponse({
        'Status': 'JSON Working:'
    })