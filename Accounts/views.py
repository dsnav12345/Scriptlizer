from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, UpdateProfile, CreateFont, EditorForm
from django.views import generic
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.models import auth
from django.contrib.auth.forms import PasswordChangeForm
from crop import cropimg
from pngsvg import pngtosvg
from svgstottf import main
from django.core.files.base import File
from django.utils.functional import lazy
from django.templatetags.static import static
import os
import ckeditor
from Scriptlizer import settings
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if User.objects.filter(username=form.data.get('username')).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=form.data.get('email')).exists():
            messages.error(request, 'Email already exists')
        elif form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.info(request, 'regestration success please login')
            name=form.data.get('username')
            os.system("mkdir Media/{}".format(name))
            os.system("mkdir Media/{}/images".format(name))
            os.system("mkdir Media/{}/svgs".format(name))
            return redirect("/login")
        return redirect("/signup")
    else:
        form = UserForm()
        print(form.media)
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("/home")
        else :
            messages.error(request, 'Invalid credentials!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.info(request, 'Please login to see your profile')
        return redirect("/login")

def editprofile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = UpdateProfile(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
            return redirect("/home")
        else:
            form = UpdateProfile(instance = request.user)
            return render(request, 'editprofile.html', {'form':form})
    else:
        messages.info(request, 'Please login to edit your profile')
        return redirect("/login")

def changepassword(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Password changed succesfully! Please login with new password')
            return redirect("/login")
        else :
            return redirect("/changepassword")
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changepassword.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect("/home")

def createfont(request):
    if request.method=='POST':
        form=CreateFont(request.POST, request.FILES)
        if form.is_valid():
            f=request.FILES['image']
            with open('Media/{}/{}.png'.format(request.user.username, request.user.username), 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)
            cropimg('Media/{}/{}.png'.format(request.user.username, request.user.username),'Media/{}/images'.format(request.user.username))
            pngtosvg('Media/{}/images'.format(request.user.username), 'Media/{}/svgs'.format(request.user.username))
            main('Media/{}/svgs'.format(request.user.username), 'static/{}.ttf'.format(request.user.username), request.user.username)
            messages.info(request, 'Font generated successfully')
        return redirect("/home")
    else:
        form=CreateFont()
        return render(request, 'createfont.html', {'downurl' : 'media/Template.png', 'form':form})

def home(request):
    fonturl='static/{}.ttf'.format(request.user.username)
    form=EditorForm()
    return render(request,'home.html',{'form':form, 'font':fonturl})