from django import forms
from .models import ContactMessage, Project

class ContactForm(forms.ModelForm):    
    class Meta:
        model= ContactMessage
        fields={
            "name",
            "email",
            "message",
        }
        labels={
            "name": "Full Name",
            "email": "Email ",
            "message": "Your Message",
        }
        widgets={
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your full name"
                }
            ),
             "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"example@gmail.com"
                }
            ),
            "message":forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Write your message here...."
                }
            ),
        }

    # For message validation (msg should be more than 20 characters)
    def clean_message(self):
        message= self.cleaned_data["message"]
        if len(message)< 20:
            raise forms.ValidationError(
                "Message must be at least 20 characters long."
            )
        return message
    
    # For name validation (name should be atleast 2 characters)
    def clean_name(self):
        name= self.cleaned_data["name"]
        if len(name)< 2:
            raise forms.ValidationError(
                "Name must contain at least 2 characters."
            )
        return name

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =[
            "title",
            "description",
            "github_link",
            "image",
            "is_featured",
        ]
        widgets={
            "title": forms.TextInput(
                attrs={
                    "placeholder":"Enter project title",
                    "class":"form-input",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder":"Describe your project",
                    "class": "form-input",
                    "rows": 5,
                }
            ),
            "github_link": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/username/project",
                    "class": "form-input",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-input",
                }
            ),
            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-checkbox",
                }
            ),
        }
        labels ={
            "title": "Project Name",
            "description":"Project Description",
            "github_link": "GitHub Repository",
            "image": "Project Image",
            "is_featured": "Featured Project",
        }

# Project title validation
def clean_title(self):
    title = self.cleaned_data["title"]
    if len(title) < 3:
        raise forms.ValidationError(
            "Project title must be at least 3 characters long."
        )
    return title

# Multiple field validation (to validate that featured project must have github repository)
def clean(self):
    cleaned_data = super().clean()

    is_featured = cleaned_data.get('is_featured')
    github_url = cleaned_data.get("github_url")

    if is_featured and not github_url:
        raise forms.ValidationError(
            "Featured projects must have a Github Repository."
        )
    return cleaned_data