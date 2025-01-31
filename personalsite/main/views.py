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

def aero(request):
    return render(request, 'aero.html')

def uprights(request):
    return render(request, 'uprights.html')

def pickleball(request):
    return render(request, 'pickleball.html')

def chess(request):
    return render(request, 'chess.html')

def sunshade(request):
    return render(request, 'sunshade.html')

def deltahand(request):
    return render(request, 'deltahand.html')

def RTR(request):
    return render(request, 'RTR.html')

def bcbets(request):
    return render(request, 'bcbets.html')

