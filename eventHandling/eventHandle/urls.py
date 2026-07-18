from django.urls import path
from eventHandle.views import user_register, event_registeration, event_list, user_list, event_handle, regiseteredEvent_list, cancelEvent, event_delete, event_update

urlpatterns = [
    # Adding all the Event Handling app URL patterns here.
    path('userRegister/', user_register, name='user_register'),
    path('event/', event_registeration, name='event_registeration'),
    path('list/', event_list, name='event_list'),
    path('userList/', user_list, name='user_list'),
    path('e-handle/', event_handle, name='event_handle'),
    path('e-registered/', regiseteredEvent_list, name='registered_event'),
    path('cancel/', cancelEvent, name='cancelEvent'),
    path('delete/', event_delete, name='event_delete'),
    path('update/', event_update, name='event_update')
]