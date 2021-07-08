from core.models import Noticia
from django.shortcuts import render
from .forms import ContactoForm,UsuariosForm,NoticiaForm

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

    return render(request,'core/Contactos.html',datos)

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

    datos ={'form' :UsuariosForm}
    
    if request.method=='POST':
        
        formulario = UsuariosForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request,'core/Registro.html',datos)

def SubirNoticia(request):

    datos ={'form' :NoticiaForm}
    
    if request.method=='POST':
        
        formulario = NoticiaForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 

    return render(request,'core/SubirNoticia.html',datos)

def Noticias(request):
    noticias = Noticia.objects.all()
    datos = {
        'noticias': noticias
    }
    return render(request,'core/Noticias.html',datos)

def Mod_Noticias(request, id):
    noticia = Noticia.objects.get(id_noticia = id)
    datos ={ 'form' : NoticiaForm(instance= noticia)}
    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST,instance= noticia)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request,'core/ModificarNoticias.html', datos)

def form_list_noticia_mod(request):   
    noticia = Noticia.objects.all()
    datos = {
        'noticia': noticia
    }
    return render(request,'core/listar_noticias_modificar.html',datos)