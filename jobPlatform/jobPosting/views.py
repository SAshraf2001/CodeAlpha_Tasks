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
    

def create_job_posting(request):
    pass

def search_job_listings(request):
    pass

def upload_resumes(request):
    pass

def apply_job(request):
    pass

def track_application(request):
    pass