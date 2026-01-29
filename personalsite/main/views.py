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

def sunshade(request):
    return render(request, 'sunshade.html')

def deltahand(request):
    return render(request, 'deltahand.html')

def RTR(request):
    return render(request, 'RTR.html')

def bcbets(request):
    return render(request, 'bcbets.html')

def hyperwatch(request):
    return render(request, 'hyperwatch.html')

def dragondock(request):
    return render(request, 'dragondock.html')

def cs238(request):
    return render(request, 'cs238.html')

def gps_navigation(request):
    return render(request, 'gps_navigation.html')

def cs140e(request):
    return render(request, 'cs140e.html')

