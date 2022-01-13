from django.shortcuts import render
from .models import Blog


def all_blogs(request):
        return render(request, 'blog/all_blogs.html') #puts all Project objects into a list
