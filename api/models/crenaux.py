from django.db import models
from .base_model import BaseModel
from .reservation import Reservation
from .service import Service
from .studio import Studio

# Table Reservation
class Crenau(BaseModel):
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE, related_name='crenau_reservation')
    dateDeb = models.DateField()
    dateFin = models.DateField()
    heureDeb = models.TimeField()
    heureFin = models.TimeField()
    notes = models.TextField(blank=True)
    statut = models.CharField(max_length=20, default='en attente')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"Reservation de {self.reservation.codeReservation} - {self.studio.nomStudio} - {self.service.nomService}"
