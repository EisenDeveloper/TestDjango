from django.contrib import admin
from .models import Noticia, Periodistas, Categoria, Contacto, Usuarios

# Register your models here.

admin.site.register(Periodistas)
admin.site.register(Usuarios)
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Noticia)