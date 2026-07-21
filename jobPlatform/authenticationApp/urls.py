from django.urls import path

from authenticationApp.views import registeredUser, loginView

urlpatterns = [
    path('sign-up/', registeredUser, name='registeredUser'),
    path('login/', loginView, name='loginView')
]