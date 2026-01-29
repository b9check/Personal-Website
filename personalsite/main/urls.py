from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    # Software & Robotics projects
    path('projects/hyperwatch/', views.hyperwatch, name='hyperwatch'),
    path('projects/dragondock/', views.dragondock, name='dragondock'),
    path('projects/pickleball/', views.pickleball, name='pickleball'),
    path('projects/deltahand/', views.deltahand, name='deltahand'),
    path('projects/bcbets/', views.bcbets, name='bcbets'),
    path('projects/cs238/', views.cs238, name='cs238'),
    path('projects/gps-navigation/', views.gps_navigation, name='gps_navigation'),
    path('projects/cs140e/', views.cs140e, name='cs140e'),
    # Mechanical projects
    path('projects/aero/', views.aero, name='aero'),
    path('projects/uprights/', views.uprights, name='uprights'),
    path('projects/sunshade/', views.sunshade, name='sunshade'),
    path('projects/RTR/', views.RTR, name='RTR'),
]