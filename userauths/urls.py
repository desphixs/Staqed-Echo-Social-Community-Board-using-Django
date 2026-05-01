from django.urls import path # Import the path tool
from . import views # Import our views

urlpatterns = [
    # The path for our registration page
    path('signup/', views.register_view, name='signup'),
    # The path for our login page
    path('signin/', views.login_view, name='signin'),
]
