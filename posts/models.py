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

# The Comment model allows users to talk to each other under a post.
class Comment(models.Model):
    # Link to the specific post this comment belongs to
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # Link to the user who wrote the comment
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # The actual text of the comment
    content = models.TextField()
    # Timestamp for when the comment was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

    def __str__(self):
        # This tells Django what to show in the Admin panel list
        return self.title
