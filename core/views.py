from django.shortcuts import render
from .models import Periodistas

# Create your views here.

def index(request):

    return render(request,'core/index.html')

def Contactos(request):

    datos ={'form' :ContactoForm}
    
    if request.method=='POST':
        
        formulario = ContactoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 

    return render(request,'core/Contactos.html')

def Deporte(request):
    return render(request,'core/Deporte.html')

def Economia(request):
    return render(request,'core/Economia.html')

def IniciarSerion(request):
    return render(request,'core/IniciarSerion.html')

def Internacional(request):
    return render(request,'core/Internacional.html')

def Nacional(request):
    return render(request,'core/Nacional.html')

def Periodistas(request):
    return render(request,'core/Periodistas.html')

def Registro(request):
    return render(request,'core/Registro.html')

def SubirNoticia(request):
    return render(request,'core/SubirNoticia.html')