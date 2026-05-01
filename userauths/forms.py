from django import forms # Import Django's form system
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Import the base forms
from .models import User # Import our custom User model

# We create our own Signup Form based on Django's UserCreationForm
class UserRegisterForm(UserCreationForm):
    # We define the email field explicitly to add our styling
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-slate-400 bg-white/50',
        'placeholder': 'Enter your email'
    }))

    # We specify which model and fields we want to use
    class Meta:
        model = User # Use our custom User model
        fields = ['email'] # We only want the email field (passwords are added automatically)
    
    # We override the __init__ method to apply styling to the password fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the same modern styling to the password inputs
        password_style = 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-slate-400 bg-white/50'
        
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({'class': password_style, 'placeholder': 'Create a password'})
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({'class': password_style, 'placeholder': 'Confirm your password'})

# We create our own Login Form based on Django's AuthenticationForm
class UserLoginForm(AuthenticationForm):
    # This runs as soon as the form is created
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We define our beautiful shared styling
        form_style = 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-slate-400 bg-white/50'
        
        # We apply the style to the username (email) and password fields
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({'class': form_style, 'placeholder': 'Enter your email'})
        if 'password' in self.fields:
            self.fields['password'].widget.attrs.update({'class': form_style, 'placeholder': 'Enter your password'})
