from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArticuloFormulario(forms.Form):

    titulo = forms.CharField(max_length=200)
    inforesumen = forms.CharField(max_length=200)
    informacion = forms.CharField(max_length=200)
    #imagen = forms.ImageField()
    #Debemos instalar Pillow

class UsuarioRegisterFormulario(UserCreationForm):

    #Datos de Usario
    email = forms.EmailField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    passwordVerify = forms.CharField(label="Verify Password", widget=forms.PasswordInput)

    #Datos Personales del Usuario
    nombre = forms.CharField(max_length=35)
    apellido = forms.CharField(max_length=35)
    celular = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    rol = forms.CharField(max_length=15) #Aquí es donde se determina si el usuario es de tipo administrador o de tipo standard
    #Foto de Perfil | Esta no necesariamente tiene que ser ingresagada a la hora de hacer el registro

    class Meta:
        model = User
        fields = ["username", "password", "passwordVerify", "email", "nombre", "apellido"]