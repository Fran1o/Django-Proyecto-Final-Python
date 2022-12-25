from django import forms
from comenapp.models import *

class ComentForm(forms.ModelForm):
    remitente = models.CharField(max_length=50)
<<<<<<< HEAD
    contenido = forms.CharField(label="Comentario")
=======
    contenido = forms.CharField(label = 'Comentario', required=True,)
>>>>>>> 50ac336557548b725455d89f2e024e6071bfa944
    class Meta:
        model = Coments
        fields = ('contenido',)
