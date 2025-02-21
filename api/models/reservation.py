from django.db import models
from .base_model import BaseModel
from .client import Client

# Table Reservation
class Reservation(BaseModel):
    codeReservation = models.CharField(max_length=50, unique=True)
    dateAdd = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    statut = models.CharField(max_length=20, default='en attente')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codeReservation
