from django.urls import path
from .views import sign_up, project_managing, sign_in
urlpatterns = [
    path('sign_up/', sign_up),
    path('sign_in/', sign_in),
    path('project_managing/', project_managing, name="managing")
]
