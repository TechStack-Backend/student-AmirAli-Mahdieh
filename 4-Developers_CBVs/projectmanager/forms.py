from django import forms
from showdetails.models import Developer
class ProjectForm(forms.Form):
    name= forms.CharField(max_length=50, required=True,label="project title", error_messages={
        "max_lenth":"projec naame must be under 50 char"
    })
    developer=forms.MultipleChoiceField(label='developers', choices=[(developer,developer) for developer in Developer.objects.all()]
                                        , widget=forms.CheckboxSelectMultiple, required=True)

    
