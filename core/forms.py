from django import forms
from django.forms import ModelForm
from .models import Noticia,Contacto,Usuarios

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['id_noticia','titulo','descripcion','imagen','id']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['email','titulo','descripcion']

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','correo','genero','edad','id']   