from django.db import models
from datetime import datetime

# Create your models here.

class Coments(models.Model):
    algo = models.CharField(max_length=30)
    remitente = models.CharField(max_length=30)
    contenido = models.CharField(max_length=1000)
    fecha = models.DateField()







