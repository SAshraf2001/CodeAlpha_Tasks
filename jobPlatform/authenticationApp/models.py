from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    roleName = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Enter the Desired Role for the User:", choices=[('isAdmin', 'Admin'), ('isRecruiter', 'Recruiter'), ('isEmployee', 'Employee')], default='Admin')
    
    def __str__(self):
        return self.roleName;

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, related_name='users', help_text='Select the Desired Role for the User:')
    
    REQUIRED_FIELDS=['email']
    
    def __str__(self):
        return self.userName