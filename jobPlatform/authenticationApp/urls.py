from django.urls import path

from authenticationApp.views import registeredUser, loginView, logoutUser

urlpatterns = [
    path('sign-up/', registeredUser, name='registeredUser'),
    path('login/', loginView, name='loginView'),
    path('sign-out/', logoutUser, name='logoutUser')
]