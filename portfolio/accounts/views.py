from django.shortcuts import render, redirect
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Register View
def register(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully!"
            )
            return redirect('register')
    else:
        form= UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user= form.get_user()

            login(request, user,)
            next_url= request.GET.get('next')
            if next_url:
                return redirect(next_url)
            messages.success(request, f"Welcome back, {user.username}!",)
            return redirect('home')
    else:
        form =AuthenticationForm()
    return render(request, "accounts/login.html",{"form":form})   

# Logout View     
def user_logout(request):
    logout(request)
    messages.success(
        request, "You have been logged out successfully!"
    )
    return redirect('home')

# Edit Profile Page
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully!"
            )
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request,"accounts/edit_profile.html",{"form":form})        
