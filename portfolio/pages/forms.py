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
        ]