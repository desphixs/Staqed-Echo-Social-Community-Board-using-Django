from django.urls import path # Import the path function to define our URLs
from . import views # Import the views from the current folder so we can link them to URLs

urlpatterns = [
    # Homepage: Leave the path empty ('') to represent the root URL
    path('', views.index, name='index'),
    
    # Detail Page: Capture a specific number (pk) to show a unique post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # Edit Page: Capture the post ID and add /edit/ to the end of the URL
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    
    # Create Page: A fixed path for the post submission form
    path('create/', views.create_post, name='create_post'),
]
