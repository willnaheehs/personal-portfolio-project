from django.contrib import admin
from .models import Project #(models.py)

# Register your models here.
#which models you want to appear in admin

admin.site.register(Project)
