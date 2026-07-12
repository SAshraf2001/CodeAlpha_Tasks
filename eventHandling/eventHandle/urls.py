from django.urls import path
from eventHandle.views import user_register, event_registeration, event_list, user_list, event_handle

urlpatterns = [
    # Adding all the Event Handling app URL patterns here.
    path('userRegister/', user_register, name='user_register'),
    path('event/', event_registeration, name='event_registeration'),
    path('list/', event_list, name='event_list'),
    path('userList/', user_list, name='user_list'),
    path('e-handle/', event_handle, name='event_handle')
]