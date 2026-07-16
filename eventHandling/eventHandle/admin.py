from django.contrib import admin
from eventHandle.models import UserRegister, EventRegister, EventHandle

# Register UserRegister simply
admin.site.register(UserRegister)

# Register EventRegister with your custom class using the decorator
@admin.register(EventRegister)
class EventRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'date', 'capacity')
    
@admin.register(EventHandle)
class EventHandleAdmin(admin.ModelAdmin):
    list_display = ('id', 'seatingCapacity', 'registeredUser', 'userTicket')