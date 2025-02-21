from django.db import models
from .base_model import BaseModel

# Les revenus de DJiman's Records
class Revenue(BaseModel):
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.month} - {self.amount} FCFA"