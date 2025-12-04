from django.shortcuts import render
from showdetails.models import Projects, Developer
from .forms import ProjectForm
# Create your views here.
def show_projects(request):
    projects=list(Projects.objects.all())
    if request.method=='GET':
        theform=ProjectForm()
        return render(request, 'projectmanager/projects_list.html', {"projects":projects, "theform": theform})
    else:
        theform=ProjectForm(request.POST)
        if theform.is_valid()==False:
            return render(request, 'projectmanager/projects_list.html', {"projects":projects, "theform": theform})
        else:
            data=theform.cleaned_data
            new_project=Projects(title=data["name"])
            new_project.save()
            for developer in data["developer"]:
                new_project.developer_set.add(Developer.objects.get(first_name= developer.split(" ")[0]))
            projects=list(Projects.objects.all())
            theform=ProjectForm()
            return render(request, 'projectmanager/projects_list.html', {"projects":projects, "theform": theform})
        