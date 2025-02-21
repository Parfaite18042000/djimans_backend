from django.db import models
from .base_model import BaseModel
from .transactions import Transaction

# Table Recu
class Recu(BaseModel):
    codeRecu = models.CharField(max_length=50, unique=True)
    dateEmission = models.DateField(auto_now_add=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reçu {self.codeRecu} - {self.transaction.codeTransaction}"
