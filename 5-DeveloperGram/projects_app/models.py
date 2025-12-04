from django.db import models

class Projects(models.Model):
    title=models.CharField(max_length=50,null=False)
    

    class Meta:
        verbose_name = ("projects")

    def __str__(self):
        return self.title

