from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog, Author

def index(request):
    context = {
        'blogs' : Blog.objects.all(),
    }
    return render(request, 'blog/blog_list.html', context)

def blog_view(request, blog_id):
    context = {
        'blog' : Blog.objects.get(pk=blog_id)
    }
    return render(request, 'blog/blog.html', context)

def author_posts_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {
        'blogs' : Blog.objects.filter(author=author)
    }
    return render(request, 'blog/blog_list.html', context)