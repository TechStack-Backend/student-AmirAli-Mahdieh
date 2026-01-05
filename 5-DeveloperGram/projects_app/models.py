from django.db import models
from django.contrib.auth.models import AbstractUser
class Projects(models.Model):
    title=models.CharField(max_length=10,null=False)
    

    class Meta:
        verbose_name = ("projects")

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    mobile=models.CharField(max_length=11, unique=True)

    USERNAME_FIELD="mobile"
    REQUIRED_FIELDS=["username"]
    def __str__(self):
        return self.nickname