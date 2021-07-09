from typing import ContextManager
from django.contrib import auth
from django.db import models
from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required, permission_required
from .models import Trabajos,mecanico,contacto

# Create your views here.

def index(request):
    return render(request,"index.html")

def atencion(request):
    return render(request,"Atencion.html")

def registro(request):
    mensaje=""
    if request.POST:
        usuario = request.POST.get("txtusuario")
        nombre = request.POST.get("txtnombre")
        correo = request.POST.get("txtcorreo")
        pass1 = request.POST.get("txtPass1")

        usu = User()
        usu.username = usuario
        usu.first_name = nombre
        usu.email = correo
        usu.set_password(pass1)
        usu.save()

        mensaje="Usuario Grabado"

    contexto = {"mensaje":mensaje}
    return render(request,"registro.html",contexto)

def trabajo(request):
    listaTrabajo=[]
    if request.POST:
        trabajo=request.POST.get("txtTrabajo")
        listaTrabajo=Trabajos.objects.filter(diagnostico__contains=trabajo)
    contexto={"listaTrabajo":listaTrabajo}
    return render(request,"trabajos.html",contexto)

@login_required(login_url='/login/')
def validar(request):
    trabajos = Trabajos.objects.all()
    contexto = {"Trabajos":trabajos}
    return render(request,"validar_post.html",contexto)

@login_required(login_url='/login/')
@permission_required('webRayoMakween.add_trabajos')
def regitra(request):
    mensaje = ""
    trabajos = Trabajos.objects.all()
    contexto = {"Trabajos":trabajos}
    if request.POST:
        diagnostico = request.POST.get("txtdiag")
        nombre = request.POST.get("txtnombre")
        fecha = request.POST.get("txtfecha")
        materiales = request.POST.get("txtmate")
        categoria = request.POST.get("txtcategoria")
        imagen= request.POST.get("txtimagen")

        tra = trabajos(
            diagnostico=diagnostico,
            nombre=nombre,
            fecha=fecha,
            materiales=materiales,
            categoria=categoria,
            imagen=imagen
        )
        tra.save()
        mensaje="Trabajo registrado"

    contexto = {"mensaje":mensaje}
    return render(request,"registro_trabajo.html",contexto)

def regico(request):
    mensaje = ""
    comentarios = contacto.objects.all()
    contexto = {"Trabajos":comentarios}
    if request.POST:
        nombre_cl=request.POST.get("txtnombre")
        correo=request.POST.get("txtcorreo")
        asunto=request.POST.get("txtasunt")
        sugerencia=request.POST.get("txtsuge")
        com = comentarios(
            nombre_cl=nombre_cl,
            correo=correo,
            asunto=asunto,
            sugerencia=sugerencia
        )
        com.save()
        mensaje="Trabajo registrado"

    contexto = {"mensaje":mensaje}
    return render(request,"Formulario_contacto.html",contexto)

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

@login_required(login_url='/login/')
@permission_required('webRayoMakween.view_trabajos')
def listra(request):
    trabajos = Trabajos.objects.all()
    contexto ={"trabajo":trabajos}
    return render(request, "listrado.html",contexto)

@login_required(login_url='/login/')
@permission_required('webRayoMakween.delete_trabajos',login_url='/login/')
def eliminar(request, id):
    try:
        tra = Trabajos.objects.get(nombre=id)
        tra.delete()
        mensaje = "Trabajo rechazado"
    except:
        mensaje = ""

    contexto = {"mensaje":mensaje}
    return render(request,"validar_post.html",contexto)

    