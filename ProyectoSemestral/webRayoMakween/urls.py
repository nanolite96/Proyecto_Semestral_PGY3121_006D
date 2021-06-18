from django.contrib import admin
from django.urls import path
from .views import atencion, contacto, index, inicio, registro, trabajos, validar

urlpatterns = [
    path('',index,name='INDEX'),
    path('atencion/',atencion,name='ATENCION'),
    path('contacto/',contacto,name='CONTACTO'),
    path('registro/',registro,name='REGISTRO'),
    path('trabajos/',trabajos,name='TRABAJOS'),
    path('validar/',validar,name='VALIDAR'),
    path('inicio/',inicio,name='INICIO')
]
