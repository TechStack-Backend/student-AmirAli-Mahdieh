from django.shortcuts import render, HttpResponseRedirect
# Create your views here.
def goto_main_page(request):
    return HttpResponseRedirect("/developers")
