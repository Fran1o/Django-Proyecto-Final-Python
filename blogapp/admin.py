from django.contrib import admin
from blogapp.models import Mascotas, RegistrarUsuario
from comenapp.models import *
# Register your models here.

admin.site.register(Mascotas)
admin.site.register(RegistrarUsuario)
admin.site.register(Coment)