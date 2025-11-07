from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Developer
from .forms import DeveloperForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
#from django.db.models import Sum, Avg, Min, Max

class show_developer(DetailView): 
    template_name="showdetails/developer_cv.html"
    model=Developer
    slug_field="last_name"
    slug_url_kwarg="last_name"


class DeveloperList (ListView):
    template_name="showdetails/developers_list.html"
    model=Developer
    context_object_name="developers"

class DeveloperCreateView(CreateView):
    model = Developer
    template_name = "showdetails/add_developer.html"
    
