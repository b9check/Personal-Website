from django.http import HttpResponse
from django.shortcuts import render


def resume(request):
    return render(request, 'resume.html')

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
