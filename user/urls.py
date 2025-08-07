"""url pattern for user app.
This file is part of the Slipher project.
and in this module we are using the Django's built-in authentication system."""


from django.urls import path, include



app_name = 'user'
urlpatterns = [
    path('',include('allauth.urls')),
]
