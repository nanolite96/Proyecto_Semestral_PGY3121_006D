from django.contrib import admin
from django.urls import path
from .views import eliminar, atencion, index, inicio, registro, trabajo, validar, regitra, regico, listra, buscar_modificar, cerrar_sesion

urlpatterns = [
    path('',index,name='INDEX'),
    path('atencion/',atencion,name='ATENCION'),
    path('contacto/',regico,name='CONTACTO'),
    path('registro/',registro,name='REGISTRO'),
    path('trabajo/',trabajo,name='TRABAJO'),
    path('validar/',validar,name='VALIDAR'),
    path('inicio/',inicio,name='INICIO'),
    path('registro_trabajos/',regitra,name='REGITRA'),
    path('listrado',listra,name='LISTRA'),
    path('eliminar/<id>/',eliminar,name="ELIMINAR"),
    path('buscar_modificar/<id>/',buscar_modificar,name="BUSMOD"),
    path('cerrar/',cerrar_sesion,name='CERRAR')

]
