from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from eventHandle.models import EventRegister, UserRegister
from authApp.models import User
from datetime import datetime
import json

# Create your views here.

@csrf_exempt
def user_register(request):
    # User Registeration before Event Placing;
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                loggedUser = request.user
                setData = json.loads(request.body)
                firstName = setData.get('First Name')
                lastName = setData.get('Last Name')
                userName = setData.get('Username')
                email = setData.get('Email')
                address = setData.get('Address')
                phoneNumber = setData.get('Phone Number')
                
                loggedUser.username = userName # Updating the Username as it is.
                loggedUser.email = email # Updating the email as it is.
                loggedUser.save() # Finally Saving the Data
                
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

def event_list(request):
    # All The Events are listed.
    return JsonResponse({
        'status': 'Passed',
        'message': "Events Listing URL is working completely:"
    })

def user_list(request):
    # All the users fetched.
    return JsonResponse({
        'status': 'Passed',
        'message': "User Listing URL is working completely:"
    })

def event_handle(request):
    # Event Handling:
    
    return JsonResponse({
        'status': 'Passed',
        'message': "Event Handling URL is working completely:"
    })