from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from ..models.user import User

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')
    
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email déjà utilisé'}, 
                       status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(
        email=email,
        username=username,
        password=password
    )
    
    return Response({
        'message': 'Inscription réussie',
        'email': user.email,
        'username': user.username
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(email=email, password=password)
    
    if user:
        return Response({
            'message': 'Connexion réussie',
            'email': user.email,
            'username': user.username
        })
    
    return Response({'error': 'Email ou mot de passe incorrect'}, 
                   status=status.HTTP_400_BAD_REQUEST)
