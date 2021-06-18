# Generated by Django 3.2.4 on 2021-06-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(null=True, primary_key=True, serialize=False, verbose_name='Id Categoria')),
                ('tipoCategoria', models.CharField(max_length=60, null=True, verbose_name='tipocategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('email', models.EmailField(max_length=254, null=True, primary_key=True, serialize=False, verbose_name='email')),
                ('titulo', models.CharField(max_length=128, null=True, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=500, null=True, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Periodistas',
            fields=[
                ('idPeriodista', models.IntegerField(null=True, primary_key=True, serialize=False, verbose_name='Id Periodista')),
                ('nombre', models.CharField(max_length=15, null=True, verbose_name='nombre')),
                ('ap_Paterno', models.CharField(max_length=15, null=True, verbose_name='Apellido Paterno')),
                ('ap_Materno', models.CharField(max_length=15, null=True, verbose_name='Apellido Materno')),
                ('edad_Periodista', models.IntegerField(verbose_name='Edad Periodista')),
                ('idCategoria', models.IntegerField(null=True, verbose_name='Id Categoria')),
                ('fecha', models.DateField(null=True, verbose_name='fecha')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.IntegerField(null=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=15, null=True, verbose_name='Nombre')),
                ('correo', models.EmailField(max_length=50, null=True, verbose_name='Email')),
                ('genero', models.CharField(max_length=9, null=True, verbose_name='genero')),
                ('edad', models.IntegerField(null=True, verbose_name='Edad')),
                ('proofesion_Periodista', models.BooleanField(verbose_name='prof_periodista')),
            ],
        ),
    ]
