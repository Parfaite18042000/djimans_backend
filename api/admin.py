from django.contrib import admin

# # Register your models here.
# from .models.base import BaseModel
from .models.user import User
from .models.client import Client
from .models.service import Service
from .models.studio import Studio
from .models.reservation import Reservation
from .models.crenaux import Crenau
from .models.facture import Facture
from .models.ligneFacture import LigneFacture
from .models.factureNormaliser import FactureNormaliser
from .models.transactions import Transaction
from .models.recu import Recu
from .models.employe import Employe
from .models.fichePaie import FicheDePaie
from .models.revenue import Revenue
from .models.tokenDGI import EMECeFToken
# # Register your models here.

# # Enregistrer les modèles
# admin.site.register(BaseModel)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Studio)
admin.site.register(Reservation)
admin.site.register(Crenau)
admin.site.register(Facture)
admin.site.register(LigneFacture)
admin.site.register(FactureNormaliser)
admin.site.register(Transaction)
admin.site.register(Employe)
admin.site.register(FicheDePaie)
admin.site.register(Recu)
admin.site.register(Revenue)
admin.site.register(EMECeFToken)