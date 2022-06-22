from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    mobile=models.CharField(max_length=10)
    pic = models.ImageField( upload_to='Profiels', blank=True)

class Font(models.Model):
    image = models.ImageField(blank=True)

class Editor(models.Model):
    body=RichTextField(blank=True, null=True)