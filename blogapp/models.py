from django.db import models

# Create your models here.

class Articulo(models.Model):

    titulo = models.CharField(max_length=200)
    inforesumen = models.CharField(max_length=200)
    informacion = models.CharField(max_length=200)
    #imagen = models.ImageField()
    #Debemos instalar Pillow

class Usuario(models.Model):

    #Datos Basicos
    email = models.EmailField()
    usuario = models.CharField(max_length=18)
    #Contraseña

    #Datos Personales
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    celular = models.IntegerField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=15) #Aquí es donde se determina si el usuario es de tipo administrador o de tipo standard
    #Foto de Perfil
