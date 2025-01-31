from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('projects/aero/', views.aero, name='aero'),
    path('projects/uprights/', views.uprights, name='uprights'),
    path('projects/pickleball/', views.pickleball, name='pickleball'),
    path('projects/chess/', views.chess, name='chess'),
    path('projects/sunshade/', views.sunshade, name='sunshade'),
    path('projects/deltahand/', views.deltahand, name='deltahand'),
    path('projects/RTR/', views.RTR, name='RTR'),
    path('projects/bcbets/', views.bcbets, name='bcbets')


]