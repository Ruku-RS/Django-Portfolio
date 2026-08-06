from django.shortcuts import render, redirect
from .models import Project, Skill
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

# Home
def home(request):
    messages.info(
                request, "Welcome to the portfolio!"
            )
    context ={
        "name": "Rukman Subedi",
        "college": "Birendra Multiple Campus",
        "semester": "8",
        "profession": "Student",
        "student": False,
        "skills":['MERN', 'SEO', 'Digital Marketing', 'Video Editing', 'SQL'],
    }
    return render(request,'pages/home.html',context)

# About
def about(request):
    return render(request,'pages/about.html')

# Contact
def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your message has been sent successfully!"
            )
            messages.error(
                request, "Something went wrong!"
            )
            messages.warning(
                request, "Your password will expire soon."
            )
            return redirect('contacts')
    else:
        form=ContactForm()

    return render(request,'pages/contact.html',{
        'form':form
    })

# Skils
def skills(request):
    skills= Skill.objects.all()

    context={
        'skills':skills
    }
    return render(request, 'pages/skills.html',context)

# Projects
def projects(request):
    projects= Project.objects.order_by("-created_at")

    context ={
        "projects": projects
    }
    return render(request,'pages/projects.html',context)

# Featured_Projects
def featured_projects(request):
    projects= Project.objects.filter(is_featured=True)
    context={
        "projects":projects
    }
    return render(request, 'pages/featured.html',context)