from django.urls import path
from authApp import views

urlpatterns = [
    # Add URL patterns of authApp.
    path('register/', views.register_user, name='register_user'), 
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user')
]