from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse('My skills!')

def projects(request):
    return HttpResponse("My Projects!")