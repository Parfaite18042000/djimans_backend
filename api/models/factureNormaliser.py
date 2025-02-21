from django.db import models
from .base_model import BaseModel
from .facture import Facture


class FactureNormaliser(BaseModel):
    codeNorm = models.CharField(max_length=50, unique=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='facture_a_normaliser')
    montantTotalHT = models.DecimalField(max_digits=10, decimal_places=2)
    montantTotalTTC = models.DecimalField(max_digits=10, decimal_places=2)
    dateEmissionDGI = models.DateField(blank=True, null=True)
    dateNormalisationDGI = models.DateField(blank=True, null=True)
    uid = models.CharField(max_length=36, unique=True, blank=True),
    counters = models.CharField(unique=True, blank=True),
    DGIstatut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En Attente de soumission'),
            ('soumise', 'Soumise à la DGI'),
            ('validee', 'Validée par la DGI'),
            ('rejetee', 'Rejetée par la DGI')
        ],
        default='en_attente'
    )  # Statut de la normalisation
    # Champ JSON pour stocker l'array de paiements
    paiements = models.CharField(max_length=100, blank=True)
    code_mecfDGI = models.CharField(max_length=29, unique=True, blank=True, null=True)  # Code MECeF renvoyé par la DGI
    qr_code = models.CharField(max_length=66, unique=True, blank=True, null=True)  # QR Code fourni par l'API e-MECeF   
    nim = models.CharField(max_length=10, unique=True, blank=True),
    errorDesc = models.CharField(unique=True, blank=True),
    def __str__(self):
        return f"Facture Normalisée {self.codeNorm}"
    