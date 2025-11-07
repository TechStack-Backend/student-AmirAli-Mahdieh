from django.urls import path
from . import views
urlpatterns = [
    path('<str:last_name>/', views.show_developer.as_view(), name="show_developers"),
    path('', views.DeveloperList.as_view(), name="main_page")
]