from re import search
from rest_framework import viewsets , filters
from clientes.seriealizer import ClientesSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class= ClientesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]
    ordering_fields =['nome']
    search_fields=['nome', 'email','cpf']
    filterset_fields=['ativo']
