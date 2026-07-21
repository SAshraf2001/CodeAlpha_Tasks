import json
from django.shortcuts import render
from authenticationApp.models import User, Role
from django.http import JsonResponse
# Create your views here.


def registeredUser(request):
    return JsonResponse({
        'Status': 'Passed and Completed',
        'Message': 'URL is working.'
    })