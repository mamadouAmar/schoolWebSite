from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DepartementModel)
admin.site.register(Professeur)
admin.site.register(Etudiant)
admin.site.register(Matiere)
admin.site.register(UE)