from django.shortcuts import render
from rest_framework import viewsets
from models import user, livre, emprunt
from serializers import userSerilizer, livreSerializer, empruntSerializer

# Create your views here.

class livreViewSet(viewsets.ModelViewSet):
    queryset = livre.objects.all().order_by('-id')
    serializer_class = livreSerializer  

class empruntViewSet(viewsets.ModelViewSet):
    queryset = emprunt.objects.all()
    serializer_class = empruntSerializer  