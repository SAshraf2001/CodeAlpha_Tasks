from django.db import models
from authApp.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class EventRegister(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, help_text='Enter the Event Title')
    place = models.CharField(max_length=50, null=False, blank=False, help_text="Enter the Event's Place:")
    date = models.DateTimeField(default=timezone.now)
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    
    def __str__(self):
        return self.title;
    

class UserRegister(models.Model):
    firstName = models.CharField(max_length=100, null=False, blank=False, help_text='Enter your First Name:')
    lastName = models.CharField(max_length=100, null=False, blank=False, help_text='Enter your Last Name:')
    address = models.CharField(max_length=100, null=False, blank=False, help_text='Enter your Address')
    phoneNumber = models.CharField(max_length=15, null=False, blank=False, help_text='Enter Contact Number')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='AuthUser')

    def __str__(self):
        return self.firstName;
    
class EventHandle(models.Model):
    seatingCapacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    registeredUser = models.ForeignKey(UserRegister, on_delete=models.CASCADE, related_name='users')
    userTicket = models.ForeignKey(EventRegister, on_delete=models.CASCADE, related_name='Event')
    
    def __str__(self):
        return f'{self.userTicket.title}'