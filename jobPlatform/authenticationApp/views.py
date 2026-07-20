import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def home_view(request):
    return JsonResponse({
        'Status': 'Passed and Completed',
        'Message': 'URL is working.'
    })