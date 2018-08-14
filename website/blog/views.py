from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog, Author, Comment
import json

def index(request):
    context = {
        'blogs' : Blog.objects.all(),
        'user' : request.user if request.user.is_authenticated else None,
    }
    return render(request, 'blog/index.html', context)

def author_posts_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {
        'blogs' : Blog.objects.filter(author=author),
        'user' : request.user if request.user.is_authenticated else None,
    }
    return render(request, 'blog/index.html', context)

def blog_view(request, blog_id):
    context = {
        'blog' : Blog.objects.get(pk=blog_id),
        'user' : request.user if request.user.is_authenticated else None,
    }
    return render(request, 'blog/blog.html', context)

def signup_view(request):
    if request.method == 'POST':
        try:
            # reading inputs
            fullname = request.POST["fullname"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            # checking for empty fields
            assert fullname != ''
            assert username != ''
            assert email != ''
            assert password != ''
            user = User.objects.create_user(username=username, email=email, password=password, first_name=fullname)
            user.save()
            Author(user=user).save()
            return HttpResponseRedirect(reverse('index'))
        except:
            return render(request, 'blog/signup.html', {'message':'fill all the details'})
    
    return render(request, 'blog/signup.html')

def login_view(request):
    # if login attempt is made
    if request.method == 'POST':
        try:
            # taking input
            username = request.POST['username']
            password = request.POST['password']
            # checking for non empty fields
            assert username != ''
            assert password != ''
            # authenticating
            user = authenticate(username=username, password=password)
            if user is None:
                raise AssertionError
        except AssertionError:
            return render(request, 'blog/login.html', {'message':'invalid credentials'})

        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    # loading login page
    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def add_comment(request, blog_id):
    if request.method == 'POST':
        try:
            author_id = request.POST["author_id"]
            assert author_id != None
            author = Author.objects.get(pk=author_id)
            message = request.POST["comment"]
            assert message != ''
            blog = Blog.objects.get(pk=blog_id)
            assert blog != None
            comment = Comment(author=author, comment=message, blog=blog)
            comment.save()
            return HttpResponseRedirect(reverse('blog_view', kwargs={'blog_id':blog_id,}))

        except AssertionError:
            return HttpResponseRedirect(reverse('blog_view', kwargs={'blog_id':blog_id,}))

def blog_input_view(request):
    # submitting the post
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            title = request.POST['title']
            contentOrder = request.POST.get("contentOrder")
            contentItems = request.POST.getlist("myContent[]")
            contentItems = json.dumps(contentItems)
            author = request.user.author

            # saving images
            files = request.FILES.getlist("myfile[]")
            for mFile in files:
                with open('blog/static/blog/upload/' + mFile.name, 'wb+') as destination:
                    for chunk in mFile.chunks():
                        destination.write(chunk)

            Blog(title=title, body=contentItems, contentOrder=contentOrder, author=author).save()
            return HttpResponseRedirect(reverse("author_posts", kwargs={'author_id':author.id}))
        except:
            print(f"Error adding a new blog")
            return render(request, reverse("index"))


    elif request.user.is_authenticated:
        context = {
            'user' : request.user if request.user.is_authenticated else None,
        }
        return render(request, 'blog/template.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))
