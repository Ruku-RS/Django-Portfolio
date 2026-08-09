from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Skill
from .forms import ContactForm, ProjectForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

# Home
def home(request):
    
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
            messages.info(
                request, "Welcome to the portfolio!"
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
    projects= Project.objects.filter(
        owner=request.user
    ).order_by("-is_featured")

    return render(request,'pages/projects.html',{
        "projects": projects
    })

# Featured_Projects
def featured_projects(request):
    projects= Project.objects.filter(is_featured=True)
    context={
        "projects":projects
    }
    return render(request, 'pages/featured.html',context)

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')

# Project creation.
@login_required
def create_project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner= request.user
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'pages/create_project.html',{'form':form})

# Edit project
@login_required
def edit_project(request, project_id):
    project = get_object_or_404(
        Project,
        id=project_id,
        owner= request.user
    )
    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            instance=project
        )
        if form.is_valid():
            form.save()
            return redirect("projects")
    else:
        form = ProjectForm(
            instance=project
        )
    return render(
        request,
        "pages/edit_project.html",
        {
            "form": form,
            "project": project
        }
    )