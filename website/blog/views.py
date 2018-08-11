from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request, message=None):
    template = loader.get_template("blog/index.html")
    context = {
        "error_message" : message,
    }
    return HttpResponse(template.render(context, request))

def success(request):
    template = loader.get_template('blog/success.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login_view(request):
    # get user details
    username = request.POST.get("username", "none")
    password = request.POST.get("password", "none")
    # authenticate
    user = authenticate(username=username, password=password)
    # if authentication successful
    if user is not None:
        return HttpResponseRedirect(reverse('success',args=()))
    # if authentication failed
    return HttpResponseRedirect(reverse('index', args=("invalid credentials",)))

def logout_view(request):
    logout(request)
    return HttpResponse("logged out")

def register(request):
    username = request.POST.get('username', "none")
    password = request.POST.get('password', "none")
    if username == 'none' or password == 'none':
        template = loader.get_template('blog/register.html')
        context = {
            "error_message" : 'enter all the fields'
        }
        return HttpResponse(template.render(context, request))
    
    user = User.objects.create_user(username=username, password=password)
    user.save()
    return HttpResponse("successfully registered")