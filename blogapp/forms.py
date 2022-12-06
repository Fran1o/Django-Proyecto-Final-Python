from django import forms

class ArticuloFormulario(forms.Form):

    titulo = forms.CharField(max_length=200)
    inforesumen = forms.CharField(max_length=200)
    informacion = forms.CharField(max_length=200)
    #imagen = forms.ImageField()
    #Debemos instalar Pillow