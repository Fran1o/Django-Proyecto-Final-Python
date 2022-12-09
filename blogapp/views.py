from django.shortcuts import render
from blogapp.models import Articulo
from blogapp.forms import ArticuloFormulario

# Create your views here.


def crear_articulo(request):

    if request.method == "POST":

        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            articulos = Articulo(titulo=data["titulo"], inforesumen=data["inforesumen"], informacion=["informacion"])
            articulos.save()

        return render(request, "blogapp/index.html", {"articulos": articulos})

    else:

        formulario = ArticuloFormulario()

    return render(request, "blogapp/crear_articulo_form.html", {"formulario": formulario})


def mostrar_articulos(request):

    articulos = Articulo.objects.all()

    return render(request, "blogapp/mostrar_articulos.html", {"articulos": articulos})

def mostrar_articulo_completo(request, id):

    articulo = Articulo.objects.get(id=id)

    return render(request, "blogapp/mostrar_articulo_completo.html", {"articulo": articulo})

