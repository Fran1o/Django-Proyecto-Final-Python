from django import forms

class ComentForm(forms.Form):
    Titulo = forms.CharField(max_length=40)
    Remitente = forms.CharField(max_length=60)
    Destinatario = forms.CharField(max_length=60)
    Contenido = forms.CharField(max_length=1000)
    Fecha = forms.DateField()
