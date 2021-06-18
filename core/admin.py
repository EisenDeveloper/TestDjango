from django.contrib import admin
from .models import Periodistas, Categoria, Contacto, Usuarios

# Register your models here.

admin.site.register(Periodistas)
admin.site.register(Usuarios)
admin.site.register(Categoria)
admin.site.register(Contacto)