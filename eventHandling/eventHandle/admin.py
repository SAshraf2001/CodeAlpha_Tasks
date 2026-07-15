from django.contrib import admin
from eventHandle.models import UserRegister, EventRegister

# Register UserRegister simply
admin.site.register(UserRegister)

# Register EventRegister with your custom class using the decorator
@admin.register(EventRegister)
class EventRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'date', 'capacity')