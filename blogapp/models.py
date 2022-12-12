from django.db import models

# Create your models here.

class Mascotas(models.Model):

    nombre = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    raza = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='fotosmascotas', null=True, blank=True)
    

class RegistrarUsuario(models.Model):
#Datos para registar un usuario

    username = models.CharField(max_length=30)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    email = models.EmailField()
    celular = models.IntegerField()
    password = models.CharField(max_length=40)
    verifypassword = models.CharField(max_length=40)

class Contacto(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=500)

