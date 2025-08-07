from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    professions = ['Engineer', 'Doctor', 'programmer', 'Teacher', 'Scientist','student', 'Artist', 'Designer', 'Entrepreneur', 'Nurse', 'Lawyer', 'Accountant', 'Chef', 'Writer', 'Musician', 'Developer', 'Researcher', 'Consultant', 'Architect']
    profession = models.CharField(max_length=30, choices=[(p, p) for p in professions])
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)