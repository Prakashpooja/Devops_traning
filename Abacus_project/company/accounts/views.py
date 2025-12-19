from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile")

        return HttpResponse("Invalid credentials", status=401)

    return HttpResponse("Login page")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "profile.html", {"profile": profile})

def about_view(request):
    return render(request, "about.html")

def logout_view(request):
    logout(request)
    return redirect("login")
