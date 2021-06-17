from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def Contactos(request):
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