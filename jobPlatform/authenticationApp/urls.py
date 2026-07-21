from django.urls import path

from authenticationApp.views import registeredUser

urlpatterns = [
    path('sign-up/', registeredUser, name='registeredUser')
]