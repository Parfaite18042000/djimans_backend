from django.db import models
from .base_model import BaseModel
from django.utils import timezone

class Client(BaseModel):
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=255)
    ifu = models.CharField(max_length=13, unique=True, null=True, blank=True)
    typeClient = models.CharField(max_length=20)
    aibType = models.CharField(max_length=1, default='N')
    tauxAIB = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    contact = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    adresse = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.matricule:
            year = timezone.now().year
            last_client = Client.objects.filter(
                matricule__startswith=f'CLI_{year}'
            ).order_by('-matricule').first()
            
            if last_client:
                last_number = int(last_client.matricule.split('_')[-1])
                new_number = last_number + 1
            else:
                new_number = 1
            
            self.matricule = f'CLI_{year}_{str(new_number).zfill(4)}'
                
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} ({self.matricule})"
