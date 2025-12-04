import projects_app.forms as forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Projects
class sign_up_form(UserCreationForm):    
    class Meta:
        model=User
        fields=("username", "password1", "password2")
        labels={"username":"Your name", "password1":"Your Password"}

class Project_Form(forms.ModelForm):
    class Meta:
        model= Projects
        fields='__all__'

