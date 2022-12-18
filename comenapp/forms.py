from django import forms

class ComentForm(forms.Form):
    # remitente = forms.CharField(max_length=30)  
    contenido = forms.CharField(max_length=1000)
    # fecha = forms.DateField()

