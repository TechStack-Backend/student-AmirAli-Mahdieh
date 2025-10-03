from django.urls import path
from . import views
urlpatterns = [
    path('<last_name>/', views.show_developer, name="show_developers"),
    path('', views.main_page, name="main_page")
]