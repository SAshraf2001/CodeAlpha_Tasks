from django.urls import path
from jobPosting.views import userRegisteration, create_job_posting, track_application, apply_job, search_job_listings

urlpatterns = [
    path('user/', userRegisteration, name='userRegisteration'),
    path('apply/', apply_job, name='apply_job'),
    path('search/', search_job_listings, name='search_job_listings'),
    path('create/', create_job_posting, name='create_job_posting'),
    path('track/', track_application, name='track_application')
]