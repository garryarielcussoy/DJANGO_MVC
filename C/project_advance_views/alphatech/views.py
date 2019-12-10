from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Mentee, Mentor

# Create your views here.

# Index Page
def index(request):
    return render(request, 'alphatech/index.html', {})

# Blog Page
def blog(request):
    return render(request, 'alphatech/blog.html', {})

# Mentor Page
def mentor(request):
    sent = {
        'mentors' : Mentor.objects.all()
    }
    return render(request, 'alphatech/mentor.html', sent)

# Mentee Page
def mentee(request):
    sent = {
        'mentees' : Mentee.objects.all()
    }
    return render(request, 'alphatech/mentee.html', sent)

# Author Page
def author(request):
    return render(request, 'alphatech/author.html', {})