from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    path('about-me/',views.about, name='about'),

    path('contact/',views.contact, name='contacts'),

    path('skills/',views.skills, name='skills'),

    path('projects/',views.projects, name='projects'),

    path('featured/',views.featured_projects, name='featured_projects'),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('projects/create/',views.create_project, name='create_project'),

    path('projects/<int:project_id>/edit/',views.edit_project, name="edit_project"),

    path('project/<int:project_id>/delete', views.delete_project, name='delete_project'),

    path('admin/', admin.site.urls, name='admin'),

    
]