from django.urls import path
from .views import index
from .views import Contactos
from .views import Deporte
from .views import Economia
from .views import IniciarSerion
from .views import Internacional
from .views import Nacional
from .views import Periodistas
from .views import Registro
from .views import SubirNoticia
from .views import Noticias
from .views import Mod_Noticias
from .views import form_list_noticia_mod
from .views import form_noticia_eliminar

urlpatterns=[
    path('',index,name="index"),

    path('Contactos/',Contactos,name="Contactos"),
    
    path('Deporte/',Deporte,name="Deporte"),
    
    path('Economia/',Economia,name="Economia"),
    
    path('IniciarSerion/',IniciarSerion,name="IniciarSerion"),
    
    path('Internacional/',Internacional,name="Internacional"),
    
    path('Nacional/',Nacional,name="Nacional"),
    
    path('Periodistas/',Periodistas,name="Periodistas"),
    
    path('Registro/',Registro,name="Registro"),
    
    path('SubirNoticia/',SubirNoticia,name="SubirNoticia"),
    
    path('Noticias/',Noticias,name="Noticias"),

    path('ModificarNoticias/<id>',Mod_Noticias,name="ModificarNoticias"),

    path('form_list_noticia_mod/',form_list_noticia_mod,name="form_list_noticia_mod"),

    path('form_noticia_eliminar/<id>',form_noticia_eliminar,name="form_noticia_eliminar"),
]