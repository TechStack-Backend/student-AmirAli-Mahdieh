from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Developer
from .forms import DeveloperForm
#from django.db.models import Sum, Avg, Min, Max

def show_developer(request, last_name): 
    try:
        developer=Developer.objects.get(last_name=last_name)
        Developer.objects.aggregate  
        return render(request, 'showdetails/developer_cv.html', {"developer":developer})
    except:
        return HttpResponseRedirect(reverse("main_page"))  

def main_page(request):
    developers=Developer.objects.all()
    if request.method=='POST':
        theform=DeveloperForm(request.POST)
        if theform.is_valid():
            data= theform.cleaned_data
            Developer.objects.create(first_name= data["first_name"], last_name=data["last_name"], email=data["email"], age=data["age"])
            developers=Developer.objects.all()
    else:
        theform=DeveloperForm()

    return render(request, 'showdetails/developers_list.html', {"developers":developers, "theform": theform})
