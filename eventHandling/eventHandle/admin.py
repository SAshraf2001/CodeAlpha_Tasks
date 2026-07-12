from django.contrib import admin
from eventHandle.models import UserRegister, EventRegister

# Register your models here.
admin.site.register(UserRegister);
admin.site.register(EventRegister);