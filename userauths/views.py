from django.shortcuts import render, redirect # Tools to show pages and move users around
from django.contrib.auth import authenticate, login, logout # Standard Django auth tools
from django.contrib import messages # Tool to show alerts and error messages
from django.contrib.auth.decorators import login_required # Security lock for views
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm # Our custom forms

# This view handles when a user wants to leave the clubhouse
def logout_view(request):
    # We officially end the user's session (take back their badge)
    logout(request)
    # We show them the goodbye page
    return render(request, 'userauths/signout.html')

# This view handles the user registration (Signup)
def register_view(request):
    # 1. If the user clicks the "Sign Up" button (POST request)
    if request.method == 'POST':
        # We fill the form with the data they typed into the browser
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

# This view handles when a user tries to sign in
def login_view(request):
    # 1. If the user clicks the "Sign In" button (POST request)
    if request.method == 'POST':
        # We fill our custom form with the data they typed
        form = UserLoginForm(request, data=request.POST)
        # We check if the form data is valid
        if form.is_valid():
            # We grab the username (which is email in our case) and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # We ask Django to check if this user actually exists in the database
            user = authenticate(username=username, password=password)
            
            # If the user is found and the password is correct
            if user is not None:
                # We officially sign them in
                login(request, user)
                # We send them back to the homepage
                return redirect('index')
        else:
            # If the login fails, we add a "Danger" message to show on the screen
            messages.error(request, "Invalid email or password. Please try again.")
    else:
        # 2. If they just arrived at the page (GET request), show a blank form
        form = UserLoginForm()
    
    # We show the signin template and pass our form
    return render(request, 'userauths/signin.html', {'form': form})

# This view handles when a user wants to personalize their identity
@login_required
def profile_edit(request):
    # 1. If the user is submitting their changes
    if request.method == 'POST':
        # We fill the form with the POST data (text) AND the FILES data (images)
        # instance=request.user tells Django which user we are updating
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            # Save the updated information back to the database
            form.save()
            # Redirect to the dashboard to see the changes
            return redirect('dashboard')
    else:
        # 2. If visiting, show the form pre-filled with the current user's data
        form = ProfileUpdateForm(instance=request.user)
        
    return render(request, 'userauths/profile_edit.html', {'form': form})
