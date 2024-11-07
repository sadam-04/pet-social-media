from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("login", views.user_login, name="user_login"),
    path("signup", views.user_signup, name="user_signup")
]