from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Coment(models.Model):
    
    Remitente = models.ForeignKey(User, related_name="Remitente", on_delete=models.CASCADE)
    Contenido = models.CharField(max_length=1000)
    Fecha = models.DateField(default=datetime.now)
