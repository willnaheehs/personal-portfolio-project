from django.shortcuts import render
from .models import Blog #import stuff from database


def all_blogs(request):
    blogs = Blog.objects.all() #grabs all objects from the database that are Blog objects (in models file), turns them into python objects
    return render(request, 'blog/all_blogs.html', {'blogs':blogs}) #puts all Blog objects into a list

