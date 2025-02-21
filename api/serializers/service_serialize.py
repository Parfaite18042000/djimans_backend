from rest_framework import serializers
from api.models.service import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'nomService', 'descriptionService', 'PU', 'statut', 
                 'taxe', 'tauxTaxe', 'createAt', 'updateAt']
        read_only_fields = ['tauxTaxe', 'createAt', 'updateAt']
def validate_nomService(self, value):
        """
        Vérifie si un service avec ce nom existe déjà
        """
        if Service.objects.filter(nomService__iexact=value).exists():
            raise serializers.ValidationError("Un service avec ce nom existe déjà.")
        return value