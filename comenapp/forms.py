from django import forms

class ComentForm(forms.Form):
    Remitente = forms.CharField(max_length=60)  
    Contenido = forms.CharField(max_length=1000)
    Fecha = forms.DateField()
