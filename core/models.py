from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class  Usuarios(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='Id',null = True)
    nombre = models.CharField(max_length=15,verbose_name='Nombre',null = True)
    correo = models.EmailField(max_length=50,verbose_name='Email',null = True)
    genero = models.CharField(max_length=9,verbose_name='genero',null = True)
    edad = models.IntegerField(verbose_name='Edad',null = True)
    profesion_Periodista = models.BooleanField(verbose_name='prof_periodista',null = False)
    def __str__(self):
        return self.nombre

class  Contacto(models.Model):
    email       = models.EmailField(primary_key=True,verbose_name='email',null = True)
    titulo      = models.CharField(max_length=128,verbose_name='titulo',null = True)
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',null = True)       
    def __str__(self):   
        return self.titulo

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True,verbose_name='Id Categoria',null = True)
    tipoCategoria = models.CharField(max_length=60,verbose_name='tipocategoria',null = True)
    def __str__(self):   
        return self.tipoCategoria

class  Periodistas(models.Model):
    idPeriodista = models.IntegerField(primary_key=True,verbose_name='Id Periodista',null = True)
    nombre = models.CharField(max_length=15,verbose_name='nombre',null = True)
    ap_Paterno = models.CharField(max_length=15,verbose_name='Apellido Paterno',null = True)
    ap_Materno = models.CharField(max_length=15,verbose_name='Apellido Materno',null = True)
    edad_Periodista = models.IntegerField(verbose_name='Edad Periodista', null=False)
    idCategoria = models.IntegerField(verbose_name='Id Categoria',null = True)
    fecha = models.DateField(verbose_name='fecha',null = True)
    imagen = models.ImageField(null=True,blank=True,verbose_name='imagen')
    def __str__(self):   
        return self.nombre

class  Noticia(models.Model):
    id_noticia = models.IntegerField(primary_key=True,verbose_name='Id Noticia',null = True)
    titulo = models.CharField(max_length=200,verbose_name='titulo',null = True)
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',null = True)
    fecha = models.DateField(verbose_name='fecha',null = True)
    imagen = models.ImageField(null=True,blank=True,verbose_name='imagen')
    def __str__(self):   
        return self.titulo