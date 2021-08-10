from django.urls import path 
from .views import *


urlpatterns = [
    path('', afficher_index, name="index"),
    path('about/', about, name="about"),
]
