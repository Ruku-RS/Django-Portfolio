from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Skill
from .forms import ContactForm, ProjectForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)

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

# Projects List View
class ProjectListView(ListView):
    model= Project
    template_name ='pages/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.order_by('-is_featured')

# Project Detail View
class ProjectDetailView(DetailView):
    model= Project
    template_name= 'pages/project_detail.html'
    context_object_name= 'project'

# Project create view
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model= Project
    form_class= ProjectForm
    template_name= 'pages/create_project.html'
    success_url ='/projects/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

# Featured_Projects
def featured_projects(request):
    projects= Project.sobjects.filter(is_featured=True)
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
    if not request.user.has_perm("pages.add_project"):
        raise PermissionDenied
    
    if request.method=='POST':
        form = ProjectForm(
            request.POST,
            request.FILES,
            )
        if form.is_valid():
            project = form.save(commit=False)
            project.owner= request.user
            project.save()
            messages.success(
                request, "Project created successfully!"
            )
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
            request.FILES,
            instance=project
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Project updated successfully!"
            )
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

# Delete Project
@login_required
def delete_project(request, project_id):
    project= get_object_or_404(
        Project,
        id= project_id,
        owner= request.user
    )
    if request.method=='POST':
        project.delete()
        messages.success(
            request,
            "Project deleted successfully!"
        )
        return redirect('projects')
    return render(
        request, 'pages/delete_project.html',{
            "project":project
        }
    )