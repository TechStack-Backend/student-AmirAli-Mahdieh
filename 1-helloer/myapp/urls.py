from django.urls import path
from . import views
urlpatterns = [
    path('',views.message),
    path('hello/',views.message),
]