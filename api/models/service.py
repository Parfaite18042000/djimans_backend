from django.db import models
from .base_model import BaseModel

# Table Services
class Service(BaseModel):
    nomService = models.CharField(max_length=255)
    descriptionService = models.TextField(blank=True)  # Description facultative)
    PU = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.BooleanField(default=True)
    # Ajout du groupe de taxation avec les nouvelles catégories
    TAXE_CHOICES = [
        ('A', 'Exonéré'),  # Exonéré (rare pour les services musicaux)
        ('B', 'Taxable (18%)'),  # Taxable standard à 18%
        ('C', 'Exportation (0%)'),  # Exportation (0%) pour clients étrangers
        ('D', 'TVA régime d’exception (18%)'),  # TVA régime d’exception pour certaines entreprises
        ('E', 'Régime fiscal TPS'),  # Régime fiscal TPS, rarement utilisé
        ('F', 'Réservé')  # Réservé, pas applicable dans la majorité des cas
    ]
    
    taxe = models.CharField(
        max_length=1,
        choices=TAXE_CHOICES,
        default='B'  # Par défaut, on considère que c'est taxable (B)
    )
    tauxTaxe = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        default=18.00,  # Par défaut, taux à 18% pour les services taxables
        help_text="Le taux de TVA ou de taxe associé au service")
    def __str__(self):
        return self.nomService
    
    def save(self, *args, **kwargs):
        # Assigner le taux basé sur le type de taxe
        if self.taxe == 'A':
            self.tauxTaxe = 0.00  # Exonéré
        elif self.taxe == 'B':
            self.tauxTaxe = 18.00  # Taxable à 18%
        elif self.taxe == 'C':
            self.tauxTaxe = 0.00  # Exportation (0%)
        elif self.taxe == 'D':
            self.tauxTaxe = 18.00  # TVA régime d’exception (18%)
        elif self.taxe == 'E':
            self.tauxTaxe = 0.00  # Régime fiscal TPS (0%)
        else:
            self.tauxTaxe = 0.00  # Réservé (on suppose pas de taxe pour ce cas)

        super().save(*args, **kwargs)
