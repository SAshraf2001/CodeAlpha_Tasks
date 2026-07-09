from django.urls import path
from authApp import views

urlpatterns = [
    # Add URL patterns of authApp.
    path('register/', views.register_user, name='register_user')
]