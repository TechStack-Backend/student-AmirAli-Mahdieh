from django import forms

class DeveloperForm(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=254, required=False)
    age=forms.IntegerField(min_value=18, max_value=50)
