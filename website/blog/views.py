from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog, Author, Comment, Tag
import json

# home page
def index(request):
    context = {
        'blogs' : Blog.objects.all(),
        'user' : request.user if request.user.is_authenticated else None,
    }
    return render(request, 'blog/index.html', context)

# authors posts page
def author_posts_view(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {
        'blogs' : Blog.objects.filter(author=author),
        'user' : request.user if request.user.is_authenticated else None,
    }
    return render(request, 'blog/index.html', context)

# shows blog content
def blog_view(request, blog_id):
    context = {
        'blog' : Blog.objects.get(pk=blog_id),
        'user' : request.user if request.user.is_authenticated else None,
    }
    return render(request, 'blog/blog.html', context)

# sign up page and handling signup request
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

# login and handling login request
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

# handles logout request
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# handles adding comments to a blog
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

# new blog page and processes it's submission
def blog_input_view(request):
    # submitting the post
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            # title
            title = request.POST['title']
            #tags
            existingTags = json.loads(request.POST["existingTags"])
            newTags = json.loads(request.POST["newTags"])
            #content
            contentOrder = request.POST.get("contentOrder")
            contentItems = json.dumps(request.POST.getlist("myContent[]"))
            # author
            author = request.user.author

            assert contentOrder != None #blog shouldn't be empty
            assert contentOrder != ""
            assert author != None

            # saving images
            files = request.FILES.getlist("myfile[]")
            
            blog = Blog(title=title, body=contentItems, contentOrder=contentOrder, author=author, no_of_images=len(files))
            blog.save()

            # adding tags
            for tagId in existingTags:
                tag = Tag.objects.get(pk=tagId)
                blog.tags.add(tag)
                blog.save()
            
            for tagName in newTags:
                tag = Tag(name=tagName)
                tag.save()
                blog.tags.add(tag)
                blog.save()

            for i in range(len(files)):
                destination_name = 'blog/static/blog/upload/' + str(blog.id) + '_' + str(i) + '_' + files[i].name
                with open(destination_name, 'wb+') as destination:
                    for chunk in files[i].chunks():
                        destination.write(chunk)

            return HttpResponseRedirect(reverse("author_posts", kwargs={'author_id':author.id}))
        
        except AssertionError:
            print(f"Error adding new blog")
            return HttpResponseRedirect(reverse("index"))

    elif request.user.is_authenticated:
        context = {
            'user' : request.user if request.user.is_authenticated else None,
            'tags' : Tag.objects.all(),
        }
        return render(request, 'blog/write_blog.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))
