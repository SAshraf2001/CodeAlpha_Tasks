from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from eventHandle.models import EventRegister, UserRegister
from django.utils import timezone

# Create your views here.

def user_register(request):
    # User Registeration before Event Placing:
    return JsonResponse({
        'status': 'Passed',
        'message': "User Registeration URL is working completely:"
    })

def event_registeration(request):
    # Events Registeration
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