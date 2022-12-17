from django.shortcuts import render, redirect
from blogapp.models import Mascotas, Contacto, Adoptar
from blogapp.forms import MascotaFormulario, ContactoFormulario, AdoptarFormulario, User

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

    if request.method == "POST":

        formulario = MascotaFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            mascotas = Mascotas()
            mascotas.nombre = request.POST.get('nombre')
            mascotas.animal = request.POST.get('animal')
            mascotas.raza = request.POST.get('raza')
            mascotas.edad = request.POST.get('edad')
            mascotas.color = request.POST.get('color')
            mascotas.imagen = request.FILES.get('imagen')
            mascotas.save()

        return render(request, "blogapp/mostrar_articulos.html", {"mascotas": mascotas})

    else:

        return render(request, "blogapp/mostrar_articulos.html", {"mascotas": mascotas})


def mostrar_articulo_completo(request, id):

    mascotas = Mascotas.objects.get(id=id)

    return render(request, "blogapp/mostrar_articulo_completo.html", {"mascotas": mascotas})


def contacto(request):

    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            infocontacto = Contacto(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], asunto=data["asunto"], mensaje=data["mensaje"])
            infocontacto.save()

        return redirect("home")

    else:

        formulario = ContactoFormulario()

    return render(request, "blogapp/contacto.html", {"formulario": formulario})

def funcion_adoptar(request, id):

    mascotas = Mascotas.objects.get(id=id)

    if request.method == "POST":
        formulario = AdoptarFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            infoadoptante = Adoptar(nombre=data["nombre"], apellido=data["apellido"], celular=data["celular"], direccion=data["direccion"])
            infoadoptante.save()

        return redirect("adopt")

    else:

        formulario = AdoptarFormulario()

    return render(request, "blogapp/form_adoptar.html", {"formulario": formulario, "mascotas": mascotas})


def adopt(request):

    return render(request, "blogapp/adopt.html") 

def perfil_user(request):

    usuario = User.objects.all()

    return render(request, "blogapp/perfil_user.html", {"usuario": usuario}) 

