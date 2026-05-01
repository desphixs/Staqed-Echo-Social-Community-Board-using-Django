from django.urls import path # Import the path tool
from . import views # Import our views

urlpatterns = [
    # The path for our registration page
    path('signup/', views.register_view, name='signup'),
    # The path for our login page
    path('signin/', views.login_view, name='signin'),
    # The path for our logout page
    path('signout/', views.logout_view, name='signout'),
    # The path for editing the user profile
    path('profile-edit/', views.profile_edit, name='profile-edit'),
]
