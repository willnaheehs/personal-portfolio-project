from django.shortcuts import render, get_object_or_404
from .models import Blog #import stuff from database, so i can send it to template


def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #grabs all objects from the database that are Blog objects (in models file), turns them into python objects
    return render(request, 'blog/all_blogs.html', {'blogs':blogs}) #puts all Blog objects into a list

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})#whats in soft brackets is being passed forward