from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Coments(models.Model):
    
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.contenido







