from django.db import models
from .base_model import BaseModel


# Table Employes
class Employe(BaseModel):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    dateNais = models.DateField()
    lieuNais = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    poste = models.CharField(max_length=255)
    dateEmbauche = models.DateField()
    salaireMensuel = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenoms} {self.matricule}"
