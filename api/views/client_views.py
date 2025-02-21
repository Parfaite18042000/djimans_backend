from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import get_object_or_404
from api.models.client import Client
from api.serializers.client_serialize import ClientSerializer

# Configurations
CLIENT_TYPES = [
    {'value': 'ENTREPRISE', 'label': 'Entreprise'},
    {'value': 'ARTISTE', 'label': 'Artiste'},
    {'value': 'PARTICULIER', 'label': 'Particulier'},
    {'value': 'GROUPE_MUSICAL', 'label': 'Groupe Musical'}
]

AIB_TYPES = [
    {'value': 'N', 'label': 'Pas AIB', 'taux': 0},
    {'value': 'A', 'label': 'Type A', 'taux': 1},
    {'value': 'B', 'label': 'Type B', 'taux': 5}
]

AIB_DICT = {item['value']: item['taux'] for item in AIB_TYPES}

@api_view(['GET'])
def get_client_configs(request):
    """Endpoint pour récupérer les configurations"""
    return Response({
        'clientTypes': CLIENT_TYPES,
        'aibTypes': AIB_TYPES
    })

@api_view(['GET'])
def get_clients(request):
    """Récupérer la liste des clients avec pagination et recherche"""
    search = request.GET.get('search', '')
    page = int(request.GET.get('page', 1))
    per_page = 10

    queryset = Client.objects.filter(deleteAt__isnull=True).filter(
        Q(nom__icontains=search) |
        Q(matricule__icontains=search) |
        Q(contact__icontains=search) |
        Q(email__icontains=search)
    ).order_by('-createAt')

    paginator = Paginator(queryset, per_page)
    clients = paginator.get_page(page)

    serializer = ClientSerializer(clients, many=True)
    
    return Response({
        'results': serializer.data,
        'count': paginator.count,
        'total_pages': paginator.num_pages
    })

@api_view(['GET'])
def get_client_by_id(request, pk):
    """Récupérer un client par son ID"""
    client = get_object_or_404(Client, pk=pk)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

@api_view(['POST'])
def create_client(request):
    """Créer un nouveau client"""
    data = request.data.copy()

    # Vérifier et assigner le taux AIB
    data['tauxAIB'] = AIB_DICT.get(data.get('aibType'), 0)

    serializer = ClientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'message': 'Erreur de validation', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_client(request, pk):
    """Mettre à jour un client existant"""
    client = get_object_or_404(Client, pk=pk)
    
    data = request.data.copy()
    if 'aibType' in data:
        data['tauxAIB'] = AIB_DICT.get(data['aibType'], client.tauxAIB)

    serializer = ClientSerializer(client, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response({'message': 'Erreur de validation', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_client(request, pk):
    """Marquer un client comme supprimé (soft delete)"""
    client = get_object_or_404(Client, pk=pk)
    client.deleteAt = timezone.now()
    client.save()
    return Response({'message': 'Client supprimé'}, status=status.HTTP_204_NO_CONTENT)
