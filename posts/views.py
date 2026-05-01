from django.shortcuts import render, redirect # Import render to show HTML pages and redirect to move users between pages
from .models import Post # Import our Post model so we can talk to the database
from .forms import PostForm # Import the PostForm we built to handle user input

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
    # Fetch the specific post using its unique ID (pk stands for primary key)
    post = Post.objects.get(pk=pk)
    
    # Put just that one post into the context dictionary
    context = {
        'post': post # The key 'post' is what we use in post_detail.html
    }
    
    # Render the detail template with that specific post's content
    return render(request, 'posts/post_detail.html', context)

def create_post(request): # This view handles the "New Post" page
    # Check if the user is submitting the form (POST method)
    if request.method == 'POST':
        # Create a form object and fill it with the data the user typed in (request.POST)
        form = PostForm(request.POST)
        # Check if the data is valid (no missing fields, etc.)
        if form.is_valid():
            # Save the new post to the database
            form.save()
            # Redirect the user back to the home page so they can see their post
            return redirect('index')
    else:
        # If the user is just visiting the page (GET method), show a blank form
        form = PostForm()
    
    # Render the create_post.html template and pass the form object
    return render(request, 'posts/create_post.html', {'form': form})

def edit_post(request, pk): # This view handles updating an existing post
    # First, find the post the user wants to edit using its ID
    post = Post.objects.get(pk=pk)
    
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

def delete_post(request, pk): # This view handles deleting a post
    # Fetch the specific post the user wants to delete using its ID
    post = Post.objects.get(pk=pk)
    
    # Check if the user confirmed the deletion (POST method)
    if request.method == 'POST':
        # Delete the post from the database
        post.delete()
        # Redirect back to the home page after deletion
        return redirect('index')
    
    # If it's a GET request, show the confirmation page
    return render(request, 'posts/delete_post.html', {'post': post})
