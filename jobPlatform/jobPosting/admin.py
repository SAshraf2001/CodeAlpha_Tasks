from django.contrib import admin
from jobPosting.models import UserProfile, jobPosting

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'First Name', 'Last Name')
    

@admin.regist(jobPosting)
class jobPostingAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Job Description')