from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('logout', views.logout, name='logout'),
    path('home',views.home,name='home'),
    path('createfont',views.createfont,name='createfont'),
]
