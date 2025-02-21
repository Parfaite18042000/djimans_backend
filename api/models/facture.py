from django.db import models
from .base_model import BaseModel
from .client import Client
from .reservation import Reservation

# Table Facture
class Facture(BaseModel):
    codeFacture = models.CharField(max_length=50, unique=True)
    dateEmissionPF = models.DateField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En Attente'),
            ('accompte_payee', 'Accompte Payee'),
            ('payee', 'Payee'),
            ('annulee', 'Annulee')
        ],
        default='en_attente'
    )  # Statut de la facture
    modePaiement = models.CharField(max_length=20, 
        choices=[
            ('cash', 'Cash'),
            ('par_tranche', 'Par Tranche'),
            ('credit', 'Crédit')
        ],
        default='cash')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Facture {self.codeFacture} - Client: {self.client.nom}"
    
    def get_montant_total_ht(self):
        """Calcule dynamiquement le montant total HT"""
        return sum(ligne.prixHT for ligne in self.lignes_factures.all())
