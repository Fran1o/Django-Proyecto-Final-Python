from django import forms
from comenapp.models import *

class ComentForm(forms.ModelForm):
    remitente = models.CharField(max_length=50)
    contenido = forms.CharField(label="Comentario")
    class Meta:
        model = Coments
        fields = ('contenido',)
