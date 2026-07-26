from django.db import models
from authenticationApp.models import User

from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class EmployeeType(models.Model):
    employeeType = models.CharField(max_length=100, blank=False, null=False, help_text='Enter the Employee Type', choices=[('full-time', "FullTime"), ('part-time', "PartTime"), ('contract', 'Contract Based'), ('intern', 'Internship')])
    
    def __str__(self):
        return self.employeeType;

class JobStatus(models.Model):
    job_status = models.CharField(max_length=100, null=False, blank=False, help_text='Enter the Job Status', choices=[('is-active', 'Active'), ('close', 'Closed'), ('under-review', 'UnderReview'), ('draft', 'Draft')])
    
    def __str__(self):
        return self.job_status;
    
class jobPosting(models.Model):
    jobTitle = models.CharField(max_length=230, blank=False, null=False)
    jobDescription = models.CharField(max_length=300, blank=False, null=False, help_text='Enter the Job Description')
    experienceLevel = models.CharField(max_length=15, blank=False, null=False)
    empType = models.ForeignKey(EmployeeType, on_delete=models.CASCADE, related_name='emp_type')
    companyName = models.CharField(max_length=200, null=False, blank=False, help_text='Enter Company Name')
    companyAddress = models.CharField(max_length=300, null=False, blank=False, help_text='Enter the Address')
    salaryPackage = models.CharField(max_length=10, null=False, blank=False, help_text='Enter the Salary Package')
    jobStatus = models.ForeignKey(JobStatus, on_delete=models.CASCADE, related_name='jobStatus')
    jobAuthor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    supportingDocuments = models.FileField(upload_to='supportDocs/', blank=True, null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    expiredDate = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.jobTitle