from django.urls import path
from jobPosting.views import userRegisteration

urlpatterns = [
    path('user/', userRegisteration, name='userRegisteration')
]