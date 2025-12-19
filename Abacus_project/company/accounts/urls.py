from django.urls import path
from .views import login_view, profile_view, about_view, logout_view

urlpatterns = [
    path("", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path("about/", about_view, name="about"),
    path("logout/", logout_view, name="logout"),
]