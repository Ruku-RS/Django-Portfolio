from django.shortcuts import render
from .models import Project


# Create your views here.


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

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def skills(request):
    return render(request, 'pages/skills.html')

def projects(request):
    projects= Project.objects.all()

    context ={
        "projects": projects
    }
    return render(request,'pages/projects.html',context)