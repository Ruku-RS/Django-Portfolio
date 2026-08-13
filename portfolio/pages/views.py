from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Skill
from .forms import ContactForm, ProjectForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)



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
class ProjectCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model= Project
    form_class= ProjectForm
    template_name= 'pages/create_project.html'
    success_url = reverse_lazy('projects')

    permission_required ='pages.add_project'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Project Update View
class ProjectUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin, UpdateView):
    model= Project
    form_class= ProjectForm
    template_name= 'pages/edit_project.html'
    success_url= '/projects/'    

    permission_required= 'pages.change_project'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

# Project Delete View
class ProjectDeleteView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin, DeleteView):
    model= Project
    template_name='pages/delete_project.html'
    success_url= reverse_lazy('projects')

    permission_required= 'pages.delete_project'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


# Featured_Projects
def feature_project(request, project_id):
    if not request.user.has_perm('pages.feature_project'):
        raise PermissionDenied

    project = get_object_or_404(
        Project,
        id = project_id
    )

    if project.is_featured:
        project.is_featured = False
        project.save()
        messages.success(
            request, 
            f'"{project.title}" has been removed from featured projects.'
        )
    else:
        project.is_featured= True
        project.save()
        messages.success(
            request,
            f'"{project.title}" has been added to featured projects.'
        )

    return redirect('projects')

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