from django.urls import path
from .views import signUp, profile, signIn
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", signUp, name='register'),
    path("register/", signUp, name='register'),
    path("login/", signIn, name='login'),
    path("logout/", signIn, name='logout'),
    path("profile", profile, name='profile'),
]
