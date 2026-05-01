from django.contrib import admin
from .models import User

# We register the User model so it shows up in our admin panel.
# This allows Sarah to manage her community members easily.
admin.site.register(User)
