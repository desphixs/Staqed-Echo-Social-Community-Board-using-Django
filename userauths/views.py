from django.shortcuts import render, redirect # Import render for HTML and redirect for moving users
from django.contrib.auth import login # Import the login function to sign users in automatically
from .forms import UserRegisterForm # Import the signup form we just built

# This view handles the user registration (Signup)
def register_view(request):
    # 1. If the user clicks the "Sign Up" button (POST request)
    if request.method == 'POST':
        # Fill the form with the data they typed
        form = UserRegisterForm(request.POST)
        # Check if everything is correct (passwords match, email is unique, etc.)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            # Log the user in immediately so they don't have to sign in again
            login(request, user)
            # Send them to the homepage to start exploring
            return redirect('index')
    else:
        # 2. If they just arrived at the page (GET request), show a blank form
        form = UserRegisterForm()
    
    # Render the signup template and pass the form object
    return render(request, 'userauths/signup.html', {'form': form})
