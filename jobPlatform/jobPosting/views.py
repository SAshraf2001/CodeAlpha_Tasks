import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def userRegisteration(request):
    try:
        if request.method == 'POST':
            pass
    except json.JSONDecodeError as err:
        return JsonResponse({
            'Status': 'Failed',
            'Message': f"Exception Caught: Error Debugged ---> {str(err)}"
        })
    
    return JsonResponse({
        'Status': 'Passed',
        'Message': "URL is Working Fine"
    })