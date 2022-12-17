from django.contrib import admin
from blogapp.models import Mascotas, Contacto, Adoptar 

# Register your models here.

admin.site.register(Mascotas)
admin.site.register(Contacto)
admin.site.register(Adoptar)