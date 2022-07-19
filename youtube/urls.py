
from django.urls import path 
from youtube import views

from django.conf import settings

urlpatterns = [
    path('', views.playlist_input, name='playlist_input' ),
           
  
]