from dataclasses import Field, field
from django.db import models
from django.forms import CharField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    avatar = models.ImageField()
    


class BlogPost(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    