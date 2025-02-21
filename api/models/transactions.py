from django.db import models
from .base_model import BaseModel
from .facture import Facture

# Table Transactions
class Transaction(BaseModel):
    codeTransaction = models.CharField(max_length=50, unique=True)
    montantPaye = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='transactions', default=1)
    typeTransac = models.CharField(
        max_length=50,
        choices=[
            ('ESPECES', 'ESPECES'),
            ('VIREMENT', 'VIREMENT'),
            ('CARTEBANCAIRE', 'CARTEBANCAIRE'),
            ('MOBILEMONEY', 'MOBILEMONEY'),
            ('CHEQUE', 'CHEQUE'),
            ('AUTRE', 'AUTRE'),
        ],
        default='ESPECES'
    )  # TYPE DE REGLEMENT
    
    def __str__(self):
        return f"Transaction {self.codeTransaction} - {self.typeTransac} - {self.facture.codeFacture}"
