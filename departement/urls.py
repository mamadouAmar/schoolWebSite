from django.urls import path 
from .views import *


urlpatterns = [
    path('tc/', afficher_index, name="TC"),
    path('gem/', afficher_index, name="GEM"),
    path('git/', afficher_index, name="GIT"),
    path('gc/', afficher_index, name="GC"),
    path('ga/', afficher_index, name="GA"),

]