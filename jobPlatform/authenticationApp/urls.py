from django.urls import path

from authenticationApp.views import registeredUser

url_patterns = [
    path('sign-up/', registeredUser, name='registeredUser')
]