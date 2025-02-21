from django.db import models
from .base_model import BaseModel
from .service import Service
from .facture import Facture

# Table LigneFacture
class LigneFacture(BaseModel):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes_factures')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    qte = models.PositiveIntegerField()
    prixHT = models.DecimalField(max_digits=10, decimal_places=2)
    prixTTC = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ligne de {self.facture.codeFacture} - {self.service.nomService}"
    
