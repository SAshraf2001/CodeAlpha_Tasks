from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="Enter the name of the role", choices=[('isAdmin', 'Admin'), ('isUser', 'User')])