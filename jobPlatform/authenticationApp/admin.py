from django.contrib import admin
from authenticationApp.models import Role, User

# Register your models here.
@admin.register(Role)
class roleAdmin(admin.ModelAdmin):
    list_display = ('id', 'roleName')
    
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [('role')]