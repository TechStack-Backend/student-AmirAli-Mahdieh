from django.shortcuts import render, HttpResponse

# Create your views here.
def message(request):
    return HttpResponse("Hello AmirAli. khaste nabashi")
