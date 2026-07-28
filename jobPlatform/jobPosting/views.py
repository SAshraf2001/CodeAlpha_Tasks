import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from jobPosting.models import UserProfile, JobStatus, jobPosting, EmployeeType, jobApply
from datetime import datetime
from django.contrib.auth.decorators import login_required
from jobPosting.decorators import admin_required, recruiter_required, employee_required
# Create your views here.
@csrf_exempt
@login_required
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
        else:
            return JsonResponse({
                'Status': "Failed to Save the Data",
                'Message': "All the Fields must be filled"
            })
    
    return JsonResponse({
        'Status': "Url Works Fine"
    })
    
@csrf_exempt
@login_required
def create_job_posting(request):
    if request.method == 'POST':
        loggedUser = request.user
        jobTitle = request.POST['Job Title']
        jobDescription = request.POST['Job Description']
        experience_level = request.POST['Experience Level']
        employeeType = request.POST['Employee Type']
        emp_type = employeeType
        empType = EmployeeType.objects.filter(employeeType=emp_type)
        if empType.exists():
            empType = empType.first()
        else:
            empType = EmployeeType.objects.create(employeeType=emp_type)
            empType.save()
        company_name = request.POST['Company Name']
        company_address = request.POST['Company Address']
        salary_package = request.POST['Salary Package']
        status = request.POST['Job Status']
        job_status = status
        jobStatus = JobStatus.objects.filter(job_status=job_status)
        created_at = request.POST['Starting Date']
        createdAt = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        expired_at = request.POST['Expiry Date']
        expiredAt = datetime.strptime(expired_at,"%Y-%m-%d %H:%M:%S" )
        supporting_docs = request.FILES['Supporting Docs']     
        if jobStatus.exists():
            jobStatus = jobStatus.first()
        else:
            JobStatus.objects.create(job_status=job_status)
        if ((jobTitle) and (jobDescription) and (experience_level) and (emp_type) and (company_name) and (company_address) and (salary_package) and(job_status) and (created_at) and (supporting_docs) and (expired_at)):
            jobPosting.objects.create(jobTitle=jobTitle, jobDescription=jobDescription, experienceLevel=experience_level, empType=empType, jobAuthor=loggedUser, createdAt=createdAt, expiredDate=expiredAt, supportingDocuments=supporting_docs, salaryPackage=salary_package, companyName=company_name, companyAddress=company_address, jobStatus=jobStatus) 
            return JsonResponse({
                'Message': "Successfully Created New Job",
                'Job Name': jobTitle,
                'Company Name': company_name
            })
        else:
            return JsonResponse({
                'Status': "Failed to create a new Job",
                'Message': "Must filled all the input Fields"
            })
        
    return JsonResponse({
        'Status': 'Passed',
        'Message': "URL works Fine"
    })

@csrf_exempt
@login_required
def search_job_listings(request):
    getJobData = jobPosting.objects.values('id', 'jobTitle', 'jobDescription')
    job_data = [] # To fill with with the extracted Data
    for item in getJobData:
        job_data.append({
            'Id': item['id'],
            'Job Title': item['jobTitle'],
            'Description': item['jobDescription']
        })
    try:
        if request.method == 'POST':
            setData = json.loads(request.body)
            searchName = setData.get('Job Name')
            searchId = setData.get('Search Id')
            
            if((searchName) and (searchId)):
                getJob = jobPosting.objects.filter(jobTitle=searchName)
                get_job_data = [] # Assigning the Extracted Data.
                for item in getJob:
                    get_job_data.append({
                        'Title': item.jobTitle,
                        'jobDescription': item.jobDescription,
                        'Company Name': item.companyName,
                        'Company Address': item.companyAddress,
                        'Experience Level': item.experienceLevel,
                        'Salary Package': item.salaryPackage,
                        'Job Status': item.jobStatus.job_status
                    })
                return JsonResponse({
                    'Message': f"Job Found: --->{searchName} && {searchId}",
                    'Details': get_job_data
                })
            else:
                return JsonResponse({
                    'Message': f'No Job Found with the specifice {searchName}'
                })
    except json.JSONDecodeError as err:
        return JsonResponse({
            'Status': 'Failed',
            'Message': f"Exception Caught: ---> {str(err)}"
        })
    return JsonResponse({
        'Status': "Passed",
        'Message': job_data
    })

@csrf_exempt
@login_required
def apply_job(request):
    pass

@csrf_exempt
@login_required
def upload_resumes(request):
    pass

def track_application(request):
    pass