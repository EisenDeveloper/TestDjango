from django import forms
from django.forms import ModelForm
from .models import Noticia,Contacto,Usuarios

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo','descripcion','imagen','id_noticia']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['email','titulo','descripcion']

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','correo','genero','edad','id']   