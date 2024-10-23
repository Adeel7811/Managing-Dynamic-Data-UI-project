from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def Home_View(request):
    return render(request, 'home/home.html')

def About_View(request):
    about = About.objects.all()
    return render(request, 'home/about.html', {'about':about})