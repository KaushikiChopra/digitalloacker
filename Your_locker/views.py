from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.template import loader
from .models import Home
from django.http import Http404
from django.http import HttpResponse






# Create your views here.
def index(request):
    if request.method=="POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            # a backend authenticated the credentials
            return redirect("/home")
        else:
            return render(request , 'Your_locker/index.html')
    return render(request , 'Your_locker/index.html')

def home(request):
    if request.user.is_anonymous:
        return redirect("/")
    all_homes = Home.objects.all()
    context ={
       'all_homes' : all_homes,
    }
    return render(request , 'Your_locker/home.html',context)

def detail(request, home_id):
    try:
        home = Home.objects.get(pk=home_id)
    except Home.DoesNotExist:
        raise Http404("This file is not found")
    return render(request , 'Your_locker/detail.html', {'home':home} )


def logoutuser(request):
    logout(request)
    return redirect("/")

class HomeCreate(CreateView):
    model = Home
    fields = ['text','home_title','upload']

def upload(request):
    return render(request , 'Your_locker/insider_form.html')

def Homes(request):
    utitle = request.POST.get('home_title')
    utext = request.POST.get('text')
    ufile = request.POST.get('upload')
    print(utitle)
    print(utext)
    h = Home(home_title=utitle , text=utext  , upload=ufile)
    h.save()
    return redirect("/home")

class HomeDelete(DeleteView):
    model = Home
    fields = ['text', 'home_title', 'upload']

    