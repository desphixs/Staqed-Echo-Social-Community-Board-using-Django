from django.shortcuts import render, redirect # Import render to show HTML pages and redirect to move users between pages
from .models import Post, Comment # Import our models
from .forms import PostForm, CommentForm # Import our forms
from django.contrib.auth.decorators import login_required # This is a "Lock" that only lets logged-in users enter a view

# Create your views here.

def index(request): # This view handles the homepage feed
    # Fetch all posts from the database, ordered by newest first (the minus sign means descending)
    posts = Post.objects.all().order_by('-created_at')
    
    # Put the database records into our context dictionary to pass them to the HTML
    context = {
        'topics': posts # The key 'topics' is what we loop through in the index.html template
    }
    
    # Render the index.html template and give it the posts data
    return render(request, 'posts/index.html', context)

def post_detail(request, pk): # This view handles the individual page for a single post
    # Fetch the specific post
    post = Post.objects.get(pk=pk)
    # Fetch all comments for this post
    comments = post.comments.all().order_by('-created_at')
    
    # Handle comment submission
    if request.method == 'POST':
        # Only logged-in users can comment
        if not request.user.is_authenticated:
            return redirect('signin')
            
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create the comment object but don't save to DB yet
            comment = form.save(commit=False)
            # Link the comment to the current post and user
            comment.post = post
            comment.user = request.user
            # Save it for real
            comment.save()
            # Refresh the page to show the new comment
            return redirect('post_detail', pk=post.pk)
    else:
        # If visiting the page, show a blank comment form
        form = CommentForm()
    
    # Combine everything for the template
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    
    return render(request, 'posts/post_detail.html', context)

@login_required # Only allow logged-in users to create posts
def create_post(request): # This view handles the "New Post" page
    # Check if the user is submitting the form (POST method)
    if request.method == 'POST':
        # Create a form object and fill it with the data the user typed in (request.POST)
        form = PostForm(request.POST)
        # Check if the data is valid (no missing fields, etc.)
        if form.is_valid():
            # 1. We tell Django: "Hold on, don't save to the database just yet!"
            post = form.save(commit=False)
            # 2. We manually sign the post by attaching the current user as the author
            post.author = request.user
            # 3. NOW we save it for real
            post.save()
            # Redirect the user back to the home page so they can see their post
            return redirect('index')
    else:
        # If the user is just visiting the page (GET method), show a blank form
        form = PostForm()
    
    # Render the create_post.html template and pass the form object
    return render(request, 'posts/create_post.html', {'form': form})

@login_required # Only allow logged-in users to edit posts
def edit_post(request, pk): # This view handles updating an existing post
    # First, find the post the user wants to edit using its ID
    post = Post.objects.get(pk=pk)
    
    # SECURITY CHECK: Only let the author edit their own post
    if post.author != request.user:
        # If they aren't the author, kick them back to the homepage
        return redirect('index')
    
    # Check if the user is submitting their changes (POST method)
    if request.method == 'POST':
        # Create a form filled with the new data AND the existing post instance
        form = PostForm(request.POST, instance=post) # instance=post tells Django to update, not create new
        # Check if the updated data is valid
        if form.is_valid():
            # Save the changes back to the database
            form.save()
            # Redirect to the post's detail page to see the updated version
            return redirect('post_detail', pk=post.pk)
    else:
        # If they are just visiting, show the form pre-filled with the current post data
        form = PostForm(instance=post) # instance=post pulls the current title/content into the inputs
        
    # Render the edit_post.html template and pass both the form and the post object
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required # Only allow logged-in users to delete posts
def delete_post(request, pk): # This view handles deleting a post
    # Fetch the specific post the user wants to delete using its ID
    post = Post.objects.get(pk=pk)
    
    # SECURITY CHECK: Only let the author delete their own post
    if post.author != request.user:
        # If they aren't the author, kick them back to the homepage
        return redirect('index')
    
    # Check if the user confirmed the deletion (POST method)
    if request.method == 'POST':
        # Delete the post from the database
        post.delete()
        # Redirect back to the home page after deletion
        return redirect('index')
    
    # If it's a GET request, show the confirmation page
    return render(request, 'posts/delete_post.html', {'post': post})
