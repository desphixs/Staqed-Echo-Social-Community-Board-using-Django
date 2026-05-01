from django.shortcuts import render
from .models import Post # Import the Post model from our models.py file

# Create your views here.

def index(request):
    # Fetch all posts from the database, ordered by newest first
    posts = Post.objects.all().order_by('-created_at')
    
    # Put the database records into our context dictionary
    context = {
        'topics': posts # We keep the name 'topics' so we don't have to change our HTML much!
    }
    
    # Render the template with the real data from the database
    return render(request, 'posts/index.html', context)
