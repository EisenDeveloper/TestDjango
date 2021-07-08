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
    
]