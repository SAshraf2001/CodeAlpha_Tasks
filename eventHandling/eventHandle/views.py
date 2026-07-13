from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from eventHandle.models import EventRegister, UserRegister
from datetime import datetime
import json

# Create your views here.

def user_register(request):
    # User Registeration before Event Placing:
    return JsonResponse({
        'status': 'Passed',
        'message': "User Registeration URL is working completely:"
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
            'Message': error
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