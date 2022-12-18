from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mascotas(models.Model):

    nombre = models.CharField(max_length=200)
    animal = models.CharField(max_length=200)
    raza = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='fotosmascotas', null=True, blank=True)

class Contacto(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=500)


class Adoptar(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.IntegerField()
    direccion = models.CharField(max_length=200)

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='fotosusuarios', null=True, blank=True)

    


