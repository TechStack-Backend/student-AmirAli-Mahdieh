from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Projects(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()
    
    class Meta:
        verbose_name = ("Projacts")

    def __str__(self):
        return self.title


class Developer(models.Model):
    first_name=models.CharField(max_length=50, db_index=True)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,null=True)
    age=models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(50)])
    projects=models.ManyToManyField(Projects)

    class Meta:
        verbose_name = "Developer"

    def __str__(self):
        return self.first_name + " " + self.last_name

class Skill (models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()
    developer= models.ForeignKey(Developer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Skill"

    def __str__(self):
        return self.title





