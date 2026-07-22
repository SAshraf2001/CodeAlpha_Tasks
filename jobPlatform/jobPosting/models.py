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
    
    
class jobPosting(models.Model):
    pass