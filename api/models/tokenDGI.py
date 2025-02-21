from django.db import models
from .base_model import BaseModel
from django.utils.timezone import now

class EMECeFToken(BaseModel):
    token = models.TextField()
    expires_at = models.DateTimeField()  # Date et heure d'expiration
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_valid_token(cls):
        token_entry = cls.objects.order_by('-created_at').first()
        if token_entry and token_entry.expires_at > now():
            return token_entry.token
        return None  # Retourne None si expiré ou non défini
