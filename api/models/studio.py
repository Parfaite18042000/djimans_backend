from django.db import models
from .base_model import BaseModel


# Table Studio
class Studio(BaseModel):
    nomStudio = models.CharField(max_length=255)
    descriptionStudio = models.TextField(blank=True) # Description facultative)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.nomStudio
