from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    path('about-me/',views.about, name='about'),

    path('contact/',views.contact, name='contacts'),

    path('skills/',views.skills, name='skills'),

    # project list view
    path('projects/', views.ProjectListView.as_view(), name='projects'),

    # project detail view (single project)
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),

    path('featured/',views.featured_projects, name='featured_projects'),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('projects/create/',views.ProjectCreateView.as_view(), name='create_project'),

    path('projects/<int:pk>/edit/',views.ProjectUpdateView.as_view(), name="edit_project"),

    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='delete_project'),
    
]