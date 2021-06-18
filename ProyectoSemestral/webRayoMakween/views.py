from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def atencion(request):
    return render(request,"Atencion.html")

def contacto(request):
    return render(request,"Formulario_contacto.html")

def registro(request):
    return render(request,"registro.html")

def trabajos(request):
    return render(request,"trabajos.html")

def validar(request):
    return render(request,"validar_post.html")

def inicio(request):
    return render(request,"inicio_sesion.html")