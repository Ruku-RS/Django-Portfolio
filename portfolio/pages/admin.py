from django.contrib import admin
from .models import Project, Skill

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "github_link",
        "created_at",
    )

    search_fields=(
        "title",
        "description",
    )

    list_filter=(
        "created_at",
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "description",
    )