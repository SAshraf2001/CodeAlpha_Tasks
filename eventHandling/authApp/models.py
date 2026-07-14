from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Enter the name of the role", choices=[('isAdmin', 'Admin'), ('isUser', 'User')], default='Admin')

    def __str__(self):
        return self.role_name


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Enter the username")
    email = models.EmailField(unique=True, null=False, blank=False, help_text="Enter the email address")
    password = models.CharField(max_length=100, null=False, blank=False, help_text="Enter the password")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, related_name='users', help_text="Select the role for the user")
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username