from django.contrib import admin
from django.urls import path
from .views import atencion, contacto, index, inicio, registro, regitra, trabajo, validar, regitra,

urlpatterns = [
    path('',index,name='INDEX'),
    path('atencion/',atencion,name='ATENCION'),
    path('contacto/',contacto,name='CONTACTO'),
    path('registro/',registro,name='REGISTRO'),
    path('trabajo/',trabajos,name='TRABAJO'),
    path('validar/',validar,name='VALIDAR'),
    path('inicio/',inicio,name='INICIO')
    path('registro_trabajos/',regitra,name='REGITRA')
]
