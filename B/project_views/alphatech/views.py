from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Index Page
def index(request):
    return render(request, 'alphatech/index.html', {})

# Blog Page
def blog(request):
    return render(request, 'alphatech/blog.html', {})

# Mentor Page
def mentor(request):
    return render(request, 'alphatech/mentor.html', {})

# Mentee Page
def mentee(request):
    return render(request, 'alphatech/mentee.html', {})

# Author Page
def author(request):
    return render(request, 'alphatech/author.html', {})