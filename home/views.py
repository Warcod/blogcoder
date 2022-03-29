from datetime import datetime
import email
from email.mime import image
from unicodedata import name
from django.shortcuts import render
from .models import BlogPost, User
from datetime import date

# Create your views here.

def home(request):
    
    user = User(name = 'Guido',
                last_name = 'Irigoyen',
                email = 'guidoirigoyen@gmail.com',
                avatar = ''
    )
    user.save()
    
    post = BlogPost(title = 'Prueba Post',
                    content = 'Loremipsuuuum',
                    date = date.today(),
                    image = '',
                    user = user
    )
    post.save()
    
    return render(request, 'home/home.html', {'title' : post.title , 'content' : post.content, 'date' : post.date})