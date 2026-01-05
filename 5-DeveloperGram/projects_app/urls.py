from django.urls import path
from .views import sign_up, project_managing, sign_in, feedback_page, home, log_out
urlpatterns = [
    path('sign_up/', sign_up, name="sign_up"),
    path('sign_in/', sign_in, name="sign_in"),
    path('project_managing/', project_managing, name="managing"),
    path('feedback/', feedback_page),
    path('', home, name='home'),
    path('logout/', log_out, name='logout'),
]
