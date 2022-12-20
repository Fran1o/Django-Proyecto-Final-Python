from django import forms
from comenapp.models import *

class ComentForm(forms.ModelForm):
    remitente = models.CharField(max_length=50)
    class Meta:
        model = Coments
        fields = ('contenido',)
