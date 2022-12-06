from django.db import models

# Create your models here.

class Articulo(models.Model):

    titulo = models.CharField(max_length=200)
    inforesumen = models.CharField(max_length=200)
    informacion = models.CharField(max_length=200)
    #imagen = models.ImageField()
    #Debemos instalar Pillow