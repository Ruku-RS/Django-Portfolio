from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="projects/",blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title= models.CharField(max_length=150)
    description= models.TextField()

    def __str__(self):
        return self.title