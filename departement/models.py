from django.db import models

#Create your models here.
class DepartementModel(models.Model):
    nom = models.CharField((""), max_length=50)
    mail = models.EmailField((""), max_length=254)
    numero = models.CharField((""), max_length=9)
    description = models.TextField((""))
    
    def __str__(self):
        return f"{self.nom}"
    
    class Meta:
        verbose_name ="Departement"
        verbose_name_plural = "Departements"
