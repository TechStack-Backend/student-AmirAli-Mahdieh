from django.contrib import admin
from .models import Developer, Projects, Skill
# Register your models here.
admin.site.register(Developer)
admin.site.register(Projects)
admin.site.register(Skill)
