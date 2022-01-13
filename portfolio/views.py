from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all() #grabs all objects from the database that are Project objects (in models file), turns them into python objects
    return render(request, 'portfolio/home.html', {'projects':projects}) #puts all Project objects into a list

