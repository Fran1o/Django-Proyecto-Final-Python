from django.shortcuts import render, redirect
from blogapp.models import Mascotas
from blogapp.forms import MascotaFormulario

# Create your views here.


def crear_articulo(request):

    if request.method == "POST":
        formulario = MascotaFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            mascotas = Mascotas(nombre=data["nombre"], animal=data["animal"], raza=data["raza"], edad=data["edad"], color=data["color"], imagen=data["imagen"] )
            mascotas.save()

        return redirect("home")

    else:

        formulario = MascotaFormulario()

    return render(request, "blogapp/crear_articulo_form.html", {"formulario": formulario})


def mostrar_articulos(request):

    mascotas = Mascotas.objects.all()

    return render(request, "blogapp/mostrar_articulos.html", {"mascotas": mascotas})

def mostrar_articulo_completo(request, id):

    mascotas = Mascotas.objects.get(id=id)

    return render(request, "blogapp/mostrar_articulo_completo.html", {"mascotas": mascotas})

