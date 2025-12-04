from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import sign_up_form, Project_Form
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Projects

from django.contrib.admin.forms import AuthenticationForm
def sign_up(request):
    if request.method == 'POST':
        the_form=sign_up_form(request.POST)
        if the_form.is_valid():
            user=the_form.save()
            login(request, user)
            return redirect(reverse("managing"))
    else:
        the_form=sign_up_form()
    return render(request, 'projects_app/sign_up.html', {"form":the_form, "the_mode":"Sign_up"})

def sign_in(request):
    if request.method == 'POST':
        the_form= AuthenticationForm(request, data= request.POST)
        if the_form.is_valid():
            user=the_form.get_user()
            login(request, user)
            return redirect("/project_managing")
    else:
        the_form=AuthenticationForm()
    return render(request, "projects_app/sign_up.html", {"form":the_form, "the_mode":"Sign_in"})

@login_required(login_url='/sign_in/')
def project_managing(request):
    if request.method =='POST':
        the_form=Project_Form(request.POST)
        if the_form.is_valid():
            the_form.save()
        return redirect("managing")
    else:
        the_form=Project_Form()
    return render(request, "projects_app/managing_page.html", {"projects":Projects.objects.all(), "the_form":the_form})
