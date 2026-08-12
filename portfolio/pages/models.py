from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Project page
class Project(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects',  
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    github_link = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="projects/",blank=True, null=True)
    
    is_featured = models.BooleanField(default=False)

    class Meta:
        permissions= [
            ("feature_project", "Can feature project")
        ]

    def __str__(self):
        return self.title

#Skill page
class Skill(models.Model):
    title= models.CharField(max_length=150)
    description= models.TextField()

    def __str__(self):
        return self.title

#Contact page
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    