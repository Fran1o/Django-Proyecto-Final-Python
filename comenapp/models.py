from django.db import models
from datetime import datetime

# Create your models here.
class Coments(models.Model):
    
    remitente = models.CharField(max_length=30)
    contenido = models.CharField(max_length=1000)
    fecha = models.DateField()

class Coments2(models.Model):
    
    remitente = models.CharField(max_length=30)
    contenido = models.CharField(max_length=1000)
    fecha = models.DateField()




