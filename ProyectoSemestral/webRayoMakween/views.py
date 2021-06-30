from typing import ContextManager
from django.contrib import auth
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required
from .models import Trabajos

# Create your views here.

def index(request):
    return render(request,"index.html")

def atencion(request):
    return render(request,"Atencion.html")

def contacto(request):
    return render(request,"Formulario_contacto.html")

def registro(request):
    return render(request,"registro.html")

def trabajo(request):
    return render(request,"trabajos.html")

def validar(request):
    return render(request,"validar_post.html")

def regitra(request):
    trabajos = Trabajos.objects.all()
    contexto = {"Trabajos":trabajos}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtdesc")
        materiales = request.POST.get("txtmate")

        tra = trabajos(
            nombre=nombre,
            descripcion=descripcion,
            materiales=materiales
        )
        tra.save()
        contexto = {"trabajos":trabajos,"mensaje":"grabo"}

    return render(request,"registro_trabajo.html",contexto)

def inicio(request):
    mensaje=" "
    if request.POST:
        nombre = request.POST.get("txtusuario")
        contra = request.POST.get("txtcontra")
        us = authenticate(request,username=nombre,password=contra)
        if us is not None and us.is_active:
            return render(request,"login.html")
        else:
            mensaje="no existe usuario o contraseña incorrecta"
    contexto={"mensaje":mensaje}
    return render(request,"login.html",contexto)