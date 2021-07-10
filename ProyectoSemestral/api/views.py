from django.shortcuts import render
from rest_framework import generics
from webRayoMakween.models import Trabajos, contacto
from .serializers import TrabajosSerializers, ContactoSerializers

# Create your views here.

class TrabajosViewSet(generics.ListAPIView):
    queryset = Trabajos.objects.all()
    serializer_class = TrabajosSerializers

class ContactoViewSet(generics.ListAPIView):
    queryset = contacto.objects.all()
    serializer_class = ContactoSerializers