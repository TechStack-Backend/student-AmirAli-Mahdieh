import projects_app.forms as forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Projects, CustomUser
from django.core.exceptions import ValidationError
class sign_in_form(AuthenticationForm):
    human=forms.BooleanField(label="i'm human", required=True)
    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].help_text="\n"
        self.fields["password"].help_text="\n"
class sign_up_form(UserCreationForm):    
    class Meta:
        model=CustomUser
        fields=("mobile","username", "password1", "password2")
        labels={"username":"Your name", "password1":"Your Password"}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text="\n"
        self.fields["password2"].help_text="\n"
        self.fields["username"].help_text="\n"
        self.fields["mobile"].help_text="\n"

class Project_Form(forms.ModelForm):
    class Meta:
        model= Projects
        fields='__all__'
        labels={"title": "project title"}
        help_texts={"title": "enter your project title"}
        error_messages={"title":{
            "max_length":"oy less than 50 char",
            "required": "it's required"
        }}

class feedback_form(forms.Form):
    suggestion=forms.CharField(label="your suggestions:",max_length=100, required=True)
    human=forms.BooleanField(label="i'm human", required=True)
    def clean_suggestion(self):
        if "shut up" in self.cleaned_data.get("suggestion").lower():
            raise ValidationError("get out")
        else:
            return self.cleaned_data.get("suggestion")
            
    # def clean(self):
    #     cleaned_data= super.clean()
    #     if cleaned_data.get("suggestion")...

    # return cleaned_data

class log_out_Form(forms.Form):
    sure=forms.BooleanField(label="I'm sure", required=True)
