from django.contrib import admin
from jobPosting.models import UserProfile, jobPosting, EmployeeType
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    

@admin.register(jobPosting)
class jobPostingAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobTitle', 'jobDescription')
    
@admin.register(EmployeeType)
class EmployeeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employeeType')