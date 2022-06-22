from django.forms import ModelForm
from django import forms
from .models import User, Font, Editor
from ckeditor.fields import RichTextField
class UserForm(ModelForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'mobile',
            'password',
            'pic',
        ]
        widgets={
            'password' : forms.PasswordInput(),
        }

class UpdateProfile(ModelForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'mobile',
            'pic',
        ]


class CreateFont(ModelForm):
    class Meta:
        model=Font
        fields=[
            'image'
        ]

class EditorForm(ModelForm):
    body=RichTextField
    class Meta:
        model=Editor
        fields=[
            'body'
        ]