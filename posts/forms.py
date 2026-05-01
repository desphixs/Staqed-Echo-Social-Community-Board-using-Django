from django import forms # Import Django's form tools
from .models import Post # Import our Post model so the form knows what data it handles

class PostForm(forms.ModelForm): # Create a class that turns our Model into a web form
    class Meta: # The Meta class tells Django the "Who" and "What" of the form
        model = Post # Tell Django this form is specifically for the Post model
        fields = ['title', 'content'] # Choose exactly which fields to show in the form
        
        # The widgets dictionary allows us to add CSS classes and placeholders to the HTML inputs
        widgets = {
            'title': forms.TextInput(attrs={ # Use a single-line text input for the title
                # Add TailwindCSS classes for a modern, rounded, and responsive look
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-slate-400 bg-white/50',
                'placeholder': 'Enter a catchy title...' # The hint text shown before typing
            }),
            'content': forms.Textarea(attrs={ # Use a multi-line box for the post content
                # Add TailwindCSS classes and set a minimum height for the text area
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 transition-all placeholder:text-slate-400 bg-white/50 min-h-[200px]',
                'placeholder': 'What is on your mind?' # The hint text shown before typing
            }),
        }
