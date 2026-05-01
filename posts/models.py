from django.db import models
from django.conf import settings # Import settings to reference our custom User model

# Create your models here.

class Post(models.Model):
    # A short title for the community post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    title = models.CharField(max_length=200)
    
    # The actual content of the post
    content = models.TextField()
    
    # Automatically set the date and time when the post is first created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This tells Django what to show in the Admin panel list
        return self.title
