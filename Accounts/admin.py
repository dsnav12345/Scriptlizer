from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'mobile', 'password']
admin.site.register(User, UserAdmin)
