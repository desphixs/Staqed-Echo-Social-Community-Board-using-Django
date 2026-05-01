from django.contrib import admin
from .models import Post

# Register your models here.

# This makes the Post model visible and editable in the Admin panel
admin.site.register(Post)
