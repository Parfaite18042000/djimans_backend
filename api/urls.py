"""
URL configuration for djimans_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.user_views import *
from .views.client_views import *
from .views.service_view import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('clients/', get_clients, name='client_list'),  # L'URL pour la liste des clients
    path('clients/<int:pk>/', get_client_by_id, name='client_detail'),  # L'URL pour le détail d'un client
    path('clients/create/', create_client, name='client_create'),  # L'URL pour la création d'un client
    path('clients/<int:pk>/update/', update_client, name='client_update'),  # L'URL pour la mise à jour d'un client
    path('clients/<int:pk>/delete/', delete_client, name='client_delete'),  # L'URL pour la suppression d'un clientpath('auth/login/', login_view, name='login'),
    path('services/', service_list, name='service_list'),
    path('services/<int:pk>/', service_detail, name='service_detail'),
    path('services/create/', create_service, name='service_create'),
    path('services/<int:pk>/update/', update_service, name='service_update'),
]
