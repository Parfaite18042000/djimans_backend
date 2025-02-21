from django.db import models
from .base_model import BaseModel
from .employe import Employe

# Table FicheDePaie
class FicheDePaie(BaseModel):
    codeFiche = models.CharField(max_length=50, unique=True)
    mois = models.CharField(max_length=20)
    montantPaye = models.DecimalField(max_digits=10, decimal_places=2)
    datePaiement = models.DateField()
    notes = models.TextField(blank=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Fiche de paie - {self.codeFiche} pour {self.employe.nom}"
