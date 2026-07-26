import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from jobPosting.models import UserProfile, JobStatus, jobPosting, EmployeeType

# Create your views here.
@csrf_exempt
def userRegisteration(request):
    if request.method == 'POST':
        logged_user = request.user
        address = request.POST['Address']
        contactNumber = request.POST['Contact Number']
        resume = request.FILES['Resume']
        userBio = request.POST['BIO']
        profilePicture = request.FILES['Profile Picture']
        portfolio = request.POST['URL']
            
        if ((address) and (contactNumber) and (resume) and (userBio) and (profilePicture) and (portfolio) and (logged_user)):    
            UserProfile.objects.create(user=logged_user, address=address, phone_number=contactNumber, resume=resume, profile_picture=profilePicture, bio=userBio, portfolio_url = portfolio)
            
            return JsonResponse({
                'Status': 'Saved Successfully',
                'Name': logged_user.username,
                'Address': address,
                'Phone Number': contactNumber,
                'User Bio': userBio,
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