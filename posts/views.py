from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

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

def post_detail(request, pk):
    # Fetch the specific post using its ID (primary key)
    post = Post.objects.get(pk=pk)
    
    context = {
        'post': post
    }
    
    return render(request, 'posts/post_detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    
    return render(request, 'posts/create_post.html', {'form': form})

