from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def skills(request):
    return HttpResponse('My skills!')

def projects(request):
    return HttpResponse("My Projects!")