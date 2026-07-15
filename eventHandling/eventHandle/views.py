# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from eventHandle.models import EventRegister, UserRegister
# from authApp.models import User
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
# Create your views here.


@csrf_exempt
@login_required
def user_register(request):
    # User Registeration before Event Placing;
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                loggedUser = request.user
                setData = json.loads(request.body)
                firstName = setData.get('First Name')
                lastName = setData.get('Last Name')
                address = setData.get('Address')
                phoneNumber = setData.get('Phone Number')
                
                UserRegister.objects.create(firstName=firstName,user=loggedUser, lastName=lastName, address=address, phoneNumber=phoneNumber)
                return JsonResponse({
                    'status' : 'The User is Authenticated and is fetched:',
                    'message': loggedUser.username,
                    'First Name': firstName,
                    'Last Name': lastName,
                    'Address': address,
                    'Contact Number': phoneNumber
                })
            else: 
                return JsonResponse({
                    'message': 'No User Found:'
                })
    except json.JSONDecodeError as error:
        return JsonResponse({
            'Status': 'Exception Caught',
            'Message': str(error)
        })
    return JsonResponse({
        'status': 'Successfull',
        'message': "Working Correctly"
    })

@csrf_exempt
@login_required
def event_registeration(request):
    # Events Registeration
    try:
        if request.method == 'POST':
            setEventData = json.loads(request.body) # Getting data fetched as requested.
            titleName = setEventData.get('Event Name')
            eventPlace = setEventData.get('Place Name')
            eventScheduled = setEventData.get('Event Date')
            eventTime = datetime.strptime(eventScheduled, "%Y-%m-%d %H:%M:%S")
            capacity = setEventData.get('Event Capacity')
            registeredEvent = EventRegister.objects.create(title=titleName, place=eventPlace, date=eventTime, capacity=capacity)
            
            registeredEvent.save()
            return JsonResponse({
                'status': "Successfully Created the Event:",
                'EventTitle': titleName,
                'Event Place': eventPlace,
                'Event Date': eventTime,
                'Seating Capacity': capacity
                })
    except json.JSONDecodeError as error: 
        return JsonResponse({
            'Status': "Exception Caught",
            'Message': str(error)
        })
    return JsonResponse({
        'status': 'Passed',
        'message': "Event Registeration URL is working completely:"
    })

@csrf_exempt
@login_required
def event_list(request):
    # All The Events are listed.
    setData = EventRegister.objects.values('title', 'place', 'date', 'capacity')
    getData = list(setData)
    event_list = [] # Appending the Data that is extracted from the getData
    for item in getData:
        event_list.append({'Name': item['title'], 'Place':item['place'], 'Date':item['date'], 'Capacity':item['capacity']})
    return JsonResponse({
        'status': 'Passed',
        'Data': event_list
    })

@csrf_exempt
@login_required
def user_list(request):
    # All the users fetched.
    setUserData = UserRegister.objects.filter() # Getting all the data filtered and passed to the said variable
    # print(setUserData) Debugging...
    user_data = [] # Appending the Fetched data.
    for item in setUserData:
        print(item.user.email)
        user_data.append({
            'First Name': item.firstName, 'Last Name': item.lastName, 'User Name':item.user.username, 'Email':item.user.email, 'Address':item.address, 'Contact Number': item.phoneNumber
        })
    # print(f'Data is fetched and is appended: ---> {user_data}') Optional to check and debug...
    return JsonResponse({
        'Status': 'Data Fetched',
        'Data': user_data
    })

def event_handle(request):
    # Event Handling:
    
    return JsonResponse({
        'status': 'Passed',
        'message': "Event Handling URL is working completely:"
    })
    

def event_update(request):
    pass


def event_delete(request):
    pass
