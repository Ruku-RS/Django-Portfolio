from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about-me/',views.about, name='about'),
    path('contact/',views.contact, name='contacts'),
    path('skills/',views.skills, name='skills'),
    path('projects/',views.projects, name='projects'),
    path('admin/', admin.site.urls, name='admin'),
]