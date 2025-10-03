from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
developers = [
    {
        "username": "hassan",
        "first_name": "Hassan",
        "last_name": "Kabiran",
        "skills": ["Python", "Django", "Vue.js"],
    },
    {
        "username": "sara",
        "first_name": "Sara",
        "last_name": "Ahmadi",
        "skills": ["JavaScript", "React", "CSS"],
    },
    {
        "username": "ali",
        "first_name": "Ali",
        "last_name": "Rezayi",
        "skills": ["Java", "Spring Boot", "SQL"],
    },
]

# Create your views here.
def show_developer(request, username): 
    for developer in developers:
        if developer["username"]==username:
            return render(request, 'showdetails/developer_cv.html', {"developer":developer})
    
    return HttpResponseRedirect(reverse("main_page"))  
def main_page(request):
    return render(request, 'showdetails/developers_list.html', {"developers":developers})
