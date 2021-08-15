from django.db import models

#Create your models here.
class DepartementModel(models.Model):
    nom = models.CharField(("nom"), max_length=50)
    mail = models.EmailField(("mail"), max_length=254)
    numero = models.CharField(("numero"), max_length=9)
    description = models.TextField(("description"))
    
    def __str__(self):
        return f"{self.nom}"
    
    class Meta:
        verbose_name ="Departement"
        verbose_name_plural = "Departements"


class Professeur(models.Model):
    contact_prof = models.PhoneNumberField(("contact"))
    date_d_adhesion = models.DateField(("Date d'adhesion"), auto_now=False, auto_now_add=False)


class Etudiant(models.Model):
    nom = models.CharField(("nom"), max_length=50)
    mail = models.EmailField(("mail"), max_length=254)
    password = models.TextField(("password"))
    date_naissance = models.DateField(("date de naissance"), auto_now=False, auto_now_add=False)
    lieu_de_naissance = models.TextField(("lieu de naissance"))


    class Meta:
        verbose_name = ("Etudiant")
        verbose_name_plural = ("Etudiants")

    def __str__(self):
        return self.nom

 
class matiere(models.Model):
    libelle = models.TextField(("Libelle"))
    code = models.TextField(("code matiere"))
    coef = models.IntegerField(("coef"))
    credit = models.IntegerField(("credit"))
    desc = models.TextField(("description"))

    class Meta:
        verbose_name = ("matiere")
        verbose_name_plural = ("matieres")

    def __str__(self):
        return self.libelle


class UE(models.Model):
    libelle = models.TextField(("libelle"))
    code = models.TextField(("code"))

    class Meta:
        verbose_name = _("UE")
        verbose_name_plural = _("UEs")

    def __str__(self):
        return self.libelle



