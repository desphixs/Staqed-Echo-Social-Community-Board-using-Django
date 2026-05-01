from django.db import models
from django.contrib.auth.models import AbstractUser

# The User model is the "Filing Folder" for every person on Echo.
class User(AbstractUser):
    # Overriding standard fields to make them optional as requested
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    
    # Custom fields for Sarah's gaming community
    full_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="user_images", default="default.jpg", null=True, blank=True)

    # Use the email as the unique identifier for logging in
    USERNAME_FIELD = 'email'
    # These fields are required when running "createsuperuser"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username) if self.username else str(self.email)
