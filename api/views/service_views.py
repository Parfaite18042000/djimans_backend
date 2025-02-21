# api/serializers/service_serializer.py
from rest_framework import serializers
from ..models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'nomService', 'descriptionService', 'PU', 'statut', 
                 'taxe', 'tauxTaxe', 'createAt', 'updateAt']
        read_only_fields = ['tauxTaxe', 'createAt', 'updateAt']

# api/views/service_views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models.service import Service
from .serialize.service import ServiceSerializer
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def service_list(request):
    if request.method == 'GET':
        try:
            services = Service.objects.all()
            serializer = ServiceSerializer(services, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'POST':
        try:
            serializer = ServiceSerializer(data=request.data)
            if serializer.is_valid():
                # L'utilisateur connecté est automatiquement défini comme createBy
                serializer.save(createBy=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def service_detail(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response({'error': 'Service non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            serializer = ServiceSerializer(service, data=request.data, partial=True)
            if serializer.is_valid():
                # L'utilisateur connecté est automatiquement défini comme updateBy
                serializer.save(updateBy=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            # Suppression logique
            service.deleteBy = request.user
            service.save()
            return Response({'message': 'Service supprimé avec succès'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)